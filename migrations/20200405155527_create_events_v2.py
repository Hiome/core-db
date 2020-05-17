from yoyo import step

__transactional__ = False

step(
  """
  create table events (
    ts bigint not null,
    topic text not null,
    namespace text not null,
    object_id text not null,
    attribute text not null,
    to_namespace text,
    to_object_id text,
    to_attribute text,
    payload json not null,
    retain boolean not null default false,
    context_ts bigint,
    context_topic text,
    primary key (ts, topic)
  )
  """,
  "drop table events"
)

step(
  """
  CREATE INDEX events_namespace ON events (namespace)
  """,
  "DROP INDEX events_namespace"
)

step(
  """
  CREATE INDEX events_object_id ON events (object_id)
  """,
  "DROP INDEX events_object_id"
)

step(
  """
  CREATE INDEX events_attribute ON events (attribute)
  """,
  "DROP INDEX events_attribute"
)

step(
  """
  CREATE INDEX events_to_namespace ON events (to_namespace) WHERE to_namespace IS NOT NULL
  """,
  "DROP INDEX events_to_namespace"
)
step(
  """
  CREATE INDEX events_to_object_id ON events (to_object_id) WHERE to_object_id IS NOT NULL
  """,
  "DROP INDEX events_to_object_id"
)
step(
  """
  CREATE INDEX events_to_attribute ON events (to_attribute) WHERE to_attribute IS NOT NULL
  """,
  "DROP INDEX events_to_attribute"
)

step(
  """
  CREATE INDEX events_context ON events (context_ts, context_topic) WHERE context_ts IS NOT NULL
  """,
  "DROP INDEX events_context"
)

step(
  """
  CREATE INDEX events_retain ON events (retain) WHERE retain IS TRUE
  """,
  "DROP INDEX events_retain"
)

step(
  """
  create table entries (
    sensor_id text not null,
    ts bigint not null,
    is_valid boolean not null,
    valid_score real not null,
    invalid_score real not null,
    confidence real not null,
    corrected boolean not null default false,
    direction text,
    sensor_conf smallint,
    bgm smallint,
    fgm smallint,
    start_position smallint,
    end_position smallint,
    history smallint,
    blob_size smallint,
    noise_size smallint,
    neighbors smallint,
    height smallint,
    width smallint,
    hw_ratio real,
    tempc smallint,
    payload json,
    primary key (sensor_id, ts)
  )
  """,
  "drop table entries"
)

step(
  """
  CREATE INDEX entries_valid ON entries (is_valid)
  """,
  "DROP INDEX entries_valid"
)

step(
  """
  CREATE INDEX entries_start_pos ON entries (start_position)
  """,
  "DROP INDEX entries_start_pos"
)

step(
  """
  CREATE INDEX entries_end_pos ON entries (end_position)
  """,
  "DROP INDEX entries_end_pos"
)
