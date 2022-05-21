import json

from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models.core import Customer, Card, Charge, Source, Refund
from .models.schedule import Schedule, Occurrence, ChargeSchedule
from .models.event import Event


class CardInline(admin.TabularInline):

    model = Card

    fields = (
        "id",
        "livemode",
        "deleted",
        "last_digits",
    )

    # classes = [
    #     "collapse",
    # ]

    extra = 0

    show_change_link = True

    can_delete = False

    def has_change_permission(self, request, obj=None):
        return False


class ChargeScheduleInline(admin.TabularInline):

    model = ChargeSchedule

    fields = [
        "id",
        "livemode",
        "human_amount",
        "currency",
        "card",
        "default_card",
        "schedule",
        "schedule_status",
        "next_occurrence_on",
        "schedule_in_words",
    ]

    readonly_fields = [
        "human_amount",
        "schedule",
        "schedule_status",
        "next_occurrence_on",
        "schedule_in_words",
    ]

    extra = 0
    can_delete = False
    show_change_link = True

    def has_change_permission(self, request, obj=None):
        return False

    def schedule(self, obj=None):
        if obj:
            return obj.schedule

    def schedule_status(self, obj=None):
        if obj:
            return obj.schedule.status

    def next_occurrence_on(self, obj=None):
        if obj and obj.schedule.next_occurrences_on:
            return obj.schedule.next_occurrences_on[0]

    def schedule_in_words(self, obj=None):
        if obj:
            return obj.schedule.in_words


class ChargeInline(admin.TabularInline):

    model = Charge
    extra = 0
    can_delete = False

    show_change_link = True

    fields = [
        "id",
        "livemode",
        "status",
        "human_amount",
        "currency",
        "refunded_amount",
        "schedule",
        "card",
        "source",
    ]

    # classes = [
    #     "collapse",
    # ]

    readonly_fields = ("human_amount",)

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    search_fields = (
        "user__email",
        "user__username",
        "id",
    )

    list_display = (
        "id",
        "deleted",
        "user",
        "livemode",
        "date_created",
        "date_updated",
    )

    readonly_fields = ("uid",)

    inlines = [
        CardInline,
        ChargeScheduleInline,
        ChargeInline,
    ]

    list_filter = (
        "livemode",
        "date_created",
        "date_updated",
        "deleted",
    )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "id",
        "livemode",
        "last_digits",
        "deleted",
        "date_created",
        "date_updated",
    )
    list_filter = (
        "livemode",
        "deleted",
        "date_created",
        "date_updated",
    )

    readonly_fields = ("uid",)
    search_fields = ("customer__user__email", "customer__user__username", "id")

    inlines = [
        ChargeInline,
    ]


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "livemode",
        "date_created",
        "charge",
        "amount",
        "currency",
        "funding_amount",
        "funding_currency",
        "voided",
    )
    list_filter = (
        "livemode",
        "date_created",
        "date_updated",
        "voided",
    )
    search_fields = [
        "charge__id",
    ]

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "livemode",
        "event_type",
        "date_created",
    )
    readonly_fields = (
        "uid",
        "event_object",
        "content_type",
        "object_id",
    )
    list_filter = ("livemode", "date_created", "date_updated", "event_type")

    fields = (
        "id",
        "livemode",
        "event_object",
        "event_type",
        "event_data",
        "uid",
        "content_type",
        "object_id",
    )

    def event_data(self, obj=None):
        return format_html("<pre>{}</pre>", json.dumps(obj.data, indent=4))

    def has_change_permission(self, request, obj=None):
        return False


class RefundInline(admin.TabularInline):
    model = Refund

    extra = 0

    fields = ["id", "livemode", "human_amount", "currency", "voided"]
    readonly_fields = ("human_amount",)

    def has_change_permission(self, request, obj=None):
        return False

    show_change_link = True


@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    search_fields = ("id",)

    def has_change_permission(self, request, obj=None):
        return False

    list_display = (
        "id",
        "livemode",
        "status",
        "date_created",
        "date_updated",
        "amount",
        # "authorize_uri",
        "authorized",
        "capturable",
        "capture",
        # "card",
        "currency",
        # "customer",
        "description",
        "disputable",
        "expired",
        "expired_at",
        "expires_at",
        "failure_code",
        "failure_message",
        "fee",
        "fee_vat",
        "funding_amount",
        "funding_currency",
        "interest",
        "interest_vat",
        "ip",
        "net",
        "paid",
        "paid_at",
        "refundable",
        "refunded_amount",
        "reversed",
        # "source",
        "voided",
        "zero_interest_installments",
    )
    list_filter = (
        "livemode",
        "date_created",
        "date_updated",
        "authorized",
        "capturable",
        "capture",
        "disputable",
        "expired",
        "expired_at",
        "expires_at",
        "paid",
        "paid_at",
        "refundable",
        "reversed",
        "voided",
        "zero_interest_installments",
    )

    inlines = [
        RefundInline,
    ]

    readonly_fields = ("uid",)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "amount",
        "bank",
        "barcode",
        "charge_status",
        "currency",
        "email",
        "flow",
        "installment_term",
        "mobile_number",
        "name",
        "phone_number",
        "platform_type",
        "receipt_amount",
        "store_id",
        "store_name",
        "terminal_id",
        "type",
        "zero_interest_installments",
    )
    list_filter = ("zero_interest_installments",)
    search_fields = (
        "id",
        "name",
    )
    readonly_fields = ("uid",)

    def has_change_permission(self, request, obj=None):
        return False
