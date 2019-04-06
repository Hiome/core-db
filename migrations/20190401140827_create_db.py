from yoyo import step

__transactional__ = False

step(
    "CREATE DATABASE hiome",
    "DROP DATABASE hiome",
)

step(
  """
  create table rooms (
    id text primary key,
    name text not null,
    occupancy_count smallint
  )
  """,
  "drop table rooms"
)

step(
  """
  create table sensors (
    id text primary key,
    room_id text,
    name text,
    type text,
    data text,
    battery real,
    last_seen timestamp,
    version text
  )
  """,
  "drop table sensors"
)

step(
  """
  create table alerts (
    source text,
    device_id text,
    message text,
    level text,
    occurred_at timestamp not null default current_timestamp
  )
  """,
  "drop table alerts"
)
