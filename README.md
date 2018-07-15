
Get list of news
[GET] 
https://shrouded-plateau-53697.herokuapp.com/news?status=draft&topic=topic1

Get news by id
[GET] 
https://shrouded-plateau-53697.herokuapp.com/news/5b4b66ce0e32000009592918

Remove news by changing status to deleted
[DELETE] 
https://shrouded-plateau-53697.herokuapp.com/news/5b4b66ce0e32000009592918

Create new news
[POST]
https://shrouded-plateau-53697.herokuapp.com/news

>  Request Params:
>  {
		"title":"title 1",
    "content":"News content 1",
    "status":"draft",
    "topics":["topic1","topic2"]
	}
