#3(a)
select max(total_value) as max_value , min(total_value) as min_value from orders;
#3(b)
select * from orders a where total_value > (select avg(total_value) from orders b where b.customer_id = a.customer_id);
#3(c)
create table customer_leaderboard(customer_id  varchar(10) references customers(customer_id), order_id int references orders(order_id), total_value float references orders(total_value),
 customer_name varchar(45) references customers(customer_name), customer_email varchar(45) references customers(customer_email));
 
 insert into customer_leaderboard(customer_id, order_id, total_value, customer_name, customer_email)
 (select c.customer_id,  x.order_id, x.total_value, c.customer_name, c.customer_email
 from customers as c
 inner join (select customer_id, max(total_value) as total_value, order_id from orders group by customer_id) x on c.customer_id = x.customer_id order by c.customer_id ); 
 
 
