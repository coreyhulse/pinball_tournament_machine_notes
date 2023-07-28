DROP TABLE IF EXISTS sandbox.machine_groups;
CREATE TABLE sandbox.machine_groups (
  machine_group_id int,
  name varchar(255),
  shortname varchar(16),
  name_sort varchar(255),
  description varchar(255),
  user_id int,
  competition_setup varchar(4000),
  competition_notes varchar(4000),
  created_at timestamp,
  updated_at timestamp,
  deleted_at timestamp
)