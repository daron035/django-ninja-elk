from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.reviews import Review as ReviewEntity


class Review(TimedBaseModel):
    customer = models.ForeignKey(
        to="customers.Customer",
        verbose_name="Reviewer",
        related_name="product_reviews",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        to="products.Product",
        verbose_name="Product",
        related_name="product_reviews",
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="User rating",
        default=1,
    )
    text = models.TextField(verbose_name="Review text", blank=True, default="")

    @classmethod
    def from_entity(
        cls,
        review: ReviewEntity,
    ) -> "Review":
        return cls(
            pk=review.id,
            customer_id=review.customer.id,
            product_id=review.product.id,
            text=review.text,
            rating=review.rating,
        )

    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(
            text=self.text,
            rating=self.rating,
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "Product review"
        verbose_name_plural = "Product reviews"
        unique_together = (("customer", "product"),)
