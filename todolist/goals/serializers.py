from django.db import transaction
from rest_framework import serializers
from core.models import User
from core.serializers import ProfileSerializer
from goals.mixins import ValidationCheckUserMixin, ValidationIsDeleteMixin
from goals.models import Board, BoardParticipant, Comment, GoalCategory, Goal



#Категории
class CategorySerializer(serializers.ModelSerializer, ValidationIsDeleteMixin):
    user = ProfileSerializer(read_only=True)
    class Meta:
        model = GoalCategory
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")


class CategoryCreateSerializer(CategorySerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    def validate_bard(self, value):
        if not BoardParticipant.objects.filter(
            board=value.get('board'),
            role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
            user=self.context["request"].user,
        ).exists():
            raise serializers.ValidationError("You not owner or writer of the related board")
        return value




#Цель
class GoalSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")


class GoalCreateSerializer(GoalSerializer, ValidationIsDeleteMixin):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    def validate_bard(self, value):
        if not BoardParticipant.objects.filter(
            board=value.get('board'),
            role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
            user=self.context["request"].user,
        ).exists():
            raise serializers.ValidationError("You not owner or writer of the related board")
        return value





#Коментарии
class CommentSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "user")

class CommentCreateSerializer(CommentSerializer, ValidationIsDeleteMixin):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    def validate_bard(self, value):
        if not BoardParticipant.objects.filter(
            board=value.get('board'),
            role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer],
            user=self.context["request"].user,
        ).exists():
            raise serializers.ValidationError("You not owner or writer of the related board")
        return value





#Доска
class BoardCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Board
        read_only_fields = ("id", "is_deleted", "created", "updated")
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.pop("user")
        board = Board.objects.create(**validated_data)
        BoardParticipant.objects.create(
            user=user, board=board, role=BoardParticipant.Role.owner
        )
        return board


class BoardParticipantSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(required=True, choices=BoardParticipant.Role.choices[1:])
    user = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = BoardParticipant
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "board")


class BoardSerializer(serializers.ModelSerializer):
    participants = BoardParticipantSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Board
        fields = "__all__"
        read_only_fields = ("id", "created", "updated")

    def update(self, instance, validated_data):
        owner = validated_data.pop("user")
        new_participants = validated_data.pop("participants")
        new_by_id = {part["user"].id: part for part in new_participants}

        old_participants = instance.participants.exclude(user=owner)
        with transaction.atomic():
            for old_participant in old_participants:
                if old_participant.user_id not in new_by_id:
                    old_participant.delete()
                else:
                    if old_participant.role != new_by_id[old_participant.user_id]["role"]:
                        old_participant.role = new_by_id[old_participant.user_id]["role"]
                        old_participant.save()
                    new_by_id.pop(old_participant.user_id)
            for new_part in new_by_id.values():
                BoardParticipant.objects.create(
                    board=instance,
                    user=new_part["user"],
                    role=new_part["role"]
                )
            if title := validated_data.get("title"):
                instance.title = title
                instance.save()
        return instance


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
