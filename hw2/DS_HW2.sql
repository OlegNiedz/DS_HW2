--Запити для виконання:

--Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
select * from tasks
where user_id = 3;

--Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
select * from tasks
WHERE status_id IN (SELECT id
    FROM status
    WHERE name = 'new');
   
--Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
  UPDATE tasks  SET status_id = 2 WHERE id = 30;
 
--Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
select * from users
where id not in (select id from tasks);

--Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
insert into tasks (title, description, status_id, user_id)
values ('My task', 'My task deskription', 1, 3);

--Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
select * from tasks
WHERE status_id IN (SELECT id
    FROM status
    WHERE name != 'completed');

--Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
   DELETE FROM tasks  WHERE id = 21;

--Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
  select * from users where email like 'ashleysimpson@example.com';

--Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
  update users set fullname = 'my user' where id = 6;

--Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
  select s.id , s."name", count(t.id) as tasks
  from tasks as t  
  left join status as s on t.status_id  = s.id
  group by s.id, s."name"
  order by s.id ;

--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
  select tasks.title as task, tasks.description, users.fullname as user, users.email
  from tasks 
  left join users on tasks.user_id = users.id 
  where users.email like '%@example.com';
 
--Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
 select * from tasks where description is null or description = '';

--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
 select u.id, u.fullname as user, t.title as task
 from users as u
 inner join tasks as t on t.user_id = u.id 
 where t.status_id in (select id from status where status."name"= 'in progress');

--Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
  select u.id , u.fullname, count(t.id) as tasks
  from tasks as t  
  left join users as u on t.user_id  = u.id
  group by u.id, u.fullname 
  order by tasks ;


