from yoyo import step

__transactional__ = False

step(
  """
  ALTER TABLE rooms ADD COLUMN hidden boolean DEFAULT FALSE
  """,
  "ALTER TABLE rooms DROP COLUMN hidden"
)
