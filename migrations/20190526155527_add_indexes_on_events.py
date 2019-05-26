from yoyo import step

__transactional__ = False

step(
  """
  CREATE INDEX logs_object_id ON logs (object_type, object_id)
  """,
  "DROP INDEX logs_object_id"
)

step(
  """
  CREATE INDEX logs_level ON logs (level) WHERE level IN ('info', 'warning', 'data')
  """,
  "DROP INDEX logs_level"
)
