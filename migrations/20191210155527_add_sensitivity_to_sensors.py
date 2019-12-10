from yoyo import step

__transactional__ = False

step(
  """
  ALTER TABLE sensors ADD COLUMN sensitivity real
  """,
  "ALTER TABLE sensors DROP COLUMN sensitivity"
)
