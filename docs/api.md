# API文档

## 接口总览

| method | url                 | note          | state       |
| ------ | ------------------- | ------------- | ----------- |
| GET    | posts               | [获取所有文章](#获取所有文章)|  |
| GET    | posts/{post_id}     | [获取单篇文章](#获取单篇文章)|  |
| GET    | tags                | [获取所有标签](#获取所有tag) | |
| GET    | tags/{tag_id}       | [获取标签详情](#获取标签详情) |    |
| GET    | tags/{tag_id}/posts | [获取标签下的文章](#获取标签下的文章) | |
| GET    | categories          | [获取所有分类](#获取所有分类) |  |
| GET    | categories/{category_id} | [获取分类详情](#获取分类详情) | |
| GET    | categories/{category_id}/posts | [获取分类详情](#获取分类详情) | |

## 获取所有文章

```
GET   /posts
```

### 参数

#### header

| Key          | value            |
| ------------ | ---------------- |
| Content-Type | application/json |


#### Payload

| key        | type | location | default | desc   |
| ---------- | ---- | -------- | ------- | ------ |
| page | int  | query | 1 | 分页 |
| size | int  | query | 20 | 每页文章数 |


### 响应

200
```json
{
    "page_size": 20,
    "current_page": 1,
    "last_page": 1,
    "count": 2,
    "data": [
        {
            "id": 1,
            "url": "http://127.0.0.1:8000/posts/1",
            "title": "this is a test",
            "views": 0,
            "summary": "this is a summary",
            "created_time": "2018-04-21T12:03:02.549099+08:00",
            "modified_time": "2018-04-21T13:35:14.895934+08:00",
            "pinned": false,
            "tags": [
                {
                    "id": 1,
                    "url": "http://127.0.0.1:8000/tags/1",
                    "name": "tag 1"
                }
            ],
            "author": {
                "id": 1,
                "nickname": "Aaron"
            }
        }
    ]
}
```


## 获取单篇文章

```
GET   /posts/{id}
```

### 参数

#### header

| Key          | value            |
| :------------ | :---------------- |
| Content-Type | application/json |


### 响应
200

```json
{
    "id": 1,
    "title": "first posts",
    "views": 0,
    "created_time": "2018-04-20T21:57:27.796133+08:00",
    "modified_time": "2018-04-20T21:57:27.796361+08:00",
    "body": "hello world",
    "tags": [
        {
            "id": 1,
            "url": "http://localhost:9000/tags/1/",
            "name": "django"
        }
    ],
}
```


## 获取所有标签

```
GET   /tags
```

### 参数

#### header

| Key          | value            |
| :------------ | :---------------- |
| Content-Type | application/json |


#### Payload

| key        | type | location | default | desc   |
| ---------- | ---- | -------- | ------- | ------ |
| page | int  | query | 1 | 分页 |
| size | int  | query | 20 | 每页标签数 |
| tag | str | query| / | 所属标签 |
| category| str | query| / | 所属分类 |


### 响应

200
```json
{
    "page_size": 20,
    "current_page": 1,
    "last_page": 1,
    "count": 2,
    "data": [
        {
            "id": 1,
            "url": "http://127.0.0.1:8000/tags/1",
            "name": "tag 1"
        }
    ]
}
```

## 获取标签详情

```
GET   /tags/{id}
```

### 参数

#### header

| Key          | value            |
| :------------ | :---------------- |
| Content-Type | application/json |


### 响应
200

```json
{
    "id": 1,
    "name": "first tag"
}
```

## 获取标签下的文章


```
GET   /tags/{id}/posts
```

### 参数

#### header

| Key          | value            |
| :------------ | :---------------- |
| Content-Type | application/json |

或

```
GET  /posts
```

#### Payload

| key        | type | location | default | desc   |
| ---------- | ---- | -------- | ------- | ------ |
| page | int  | query | 1 | 分页 |
| size | int  | query | 20 | 每页文章数 |
| tag | str | query| / | 所属标签 |

#### 响应
200

与 [获取所有文章](#获取所有文章) 相同


## 获取所有分类

```
GET   /categories
```

### 参数

#### header

| Key          | value            |
| :------------ | :---------------- |
| Content-Type | application/json |


#### Payload

| key        | type | location | default | desc   |
| ---------- | ---- | -------- | ------- | ------ |
| page | int  | query | 1 | 分页 |
| size | int  | query | 20 | 每页分类数 |


### 响应

200
```json
{
    "page_size": 20,
    "current_page": 1,
    "last_page": 1,
    "count": 2,
    "data": [
        {
            "id": 1,
            "url": "http://127.0.0.1:8000/categories/1",
            "parent_category": "parent_category",
            "name": "category 1"
        }
    ]
}
```

## 获取标签详情

```
GET   /categories/{id}
```

### 参数

#### header

| Key          | value            |
| :------------ | :---------------- |
| Content-Type | application/json |


### 响应
200

```json
{
    "id": 1,
    "name": "first category",
    "descendants": [
        {
            "id": 1,
            "url": "http://127.0.0.1:8000/categories/2",
            "name": "category 2"
        }
    ]
}
```

## 获取标签下的文章


```
GET   /categories/{id}/posts
```

### 参数

#### header

| Key          | value            |
| :------------ | :---------------- |
| Content-Type | application/json |

或

```
GET  /posts
```

#### Payload

| key        | type | location | default | desc   |
| ---------- | ---- | -------- | ------- | ------ |
| page | int  | query | 1 | 分页 |
| size | int  | query | 20 | 每页文章数 |
| category | str | query| / | 所属分类 |

#### 响应
200

与 [获取所有文章](#获取所有文章) 相同