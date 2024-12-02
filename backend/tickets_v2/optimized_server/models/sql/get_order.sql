select
  o.cached_price as total,
  p2.title,
  p2.price,
  p2.quantity,
  case
    when cancelled_at is not null then 'CANCELLED'
    when paid_at is not null then 'PAID'
    else 'CONFIRMED'
  end as status
from
  tickets_v2_order o
  join lateral (
    select
      p.title,
      p.price,
      cast(pd.value as int) as quantity
    from
      tickets_v2_product p
      join jsonb_each(o.product_data) pd on (cast(pd.key as int) = p.id)
  ) as p2 on true
where
  o.event_id = %(event_id)s
  and o.id = %(order_id)s
