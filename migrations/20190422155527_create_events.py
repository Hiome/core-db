from yoyo import step

__transactional__ = False

step(
  "DROP TABLE alerts",
  """
  CREATE TABLE alerts (
    source text,
    device_id text,
    message text,
    level text,
    occurred_at timestamp not null default current_timestamp
  )
  """
)

step(
  """
  CREATE TABLE logs (
    id bigserial primary key,
    source text,
    event_type text,
    object_type text,
    object_id text,
    message text,
    level text,
    blob text,
    occurred_at timestamp not null default current_timestamp
  )
  """,
  "DROP TABLE logs"
)
