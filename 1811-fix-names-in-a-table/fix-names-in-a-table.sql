select
    user_id, 
    concat(left(upper(name), 1), right(lower(name), length(name) - 1)) as name
from Users
    order by user_id