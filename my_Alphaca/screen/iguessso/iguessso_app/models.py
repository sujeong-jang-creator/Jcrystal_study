from django.db import models

class Results(models.Model):
    # 장고는 기본적으로 pk (Primary Key)를 생성해주는데, id 값이라고 생각하면 됨! 데이터가 추가될 때마다 자동으로 증가하는 숫자
    result_id = models.IntegerField(primary_key=True)
    register_date = models.DateField(null=False)
    img_file_path = models.TextField(null=False)
    first_grade = models.CharField(max_length=4, null=False)
    first_grade_percentage = models.IntegerField(null=False)
    second_grade = models.CharField(max_length=4, null=False)
    second_grade_percentage = models.IntegerField(null=False)
    third_grade = models.CharField(max_length=4, null=False)
    third_grade_percentage = models.IntegerField(null=False)
    modified_grade = models.CharField(max_length=4, null=True, blank=True)
    cow_sex = models.CharField(max_length=4, null=True, blank=True)
    model_id = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)

    def __str__(self):
        # return str(self.result_id)
        return self.first_grade

