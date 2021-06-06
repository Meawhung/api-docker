from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator  # new


class TextSummary(models.Model):
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


SummarySchema = pydantic_model_creator(TextSummary)  # new


# class Account(models.Model):
#     name = fields.TextField()
#     amount = fields.IntField()
#     created_at = fields.DatetimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} : {self.amount}"
