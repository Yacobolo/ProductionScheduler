# schemas.py

from ninja import ModelSchema

from api.models import Job, JobStatus, JobType


class JobIn(ModelSchema):
    job_status_id: int
    job_type_id: int

    class Config:
        model = Job
        model_fields = ["name", "customer", "due_date", "priority", "external_id"]
        # model_fields_optional = ["description", "customer", "note"]


class JobOut(ModelSchema):
    job_status_id: int
    job_type_id: int

    class Config:
        model = Job
        model_exclude = ["job_status", "job_type"]
        # model_fields = ["id", "name", "customer", "due_date", "priority", "external_id"]


class JobTypeOut(ModelSchema):
    class Config:
        model = JobType
        model_fields = ["id", "name"]


class JobStatusOut(ModelSchema):
    class Config:
        model = JobStatus
        model_fields = "__all__"
