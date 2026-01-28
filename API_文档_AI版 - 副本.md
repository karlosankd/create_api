# CMS 平台 API 参考文档 (AI 版)

本文档提供 API 接口的精简描述，适合 AI 助手快速理解和使用。

## API 快速索引

| 模块 | 接口 | 方法 | 路径 |
|------|------|------|------|
| 09. 课程分类管理 | 删除课程分类 | POST | `/api/courseClass/delete` |
| 09. 课程分类管理 | 课程分类分页 | POST | `/api/courseClass/page` |
| 09. 课程分类管理 | 保存课程分类 | POST | `/api/courseClass/save` |
| 09. 课程分类管理 | 修改课程分类 | POST | `/api/courseClass/update` |
| 10. 课程标签管理 | 删除课程标签 | POST | `/api/courseTag/delete` |
| 10. 课程标签管理 | 课程标签分页 | POST | `/api/courseTag/page` |
| 10. 课程标签管理 | 保存课程标签 | POST | `/api/courseTag/save` |
| 10. 课程标签管理 | 修改课程标签 | POST | `/api/courseTag/update` |
| 12. 课程管理 | 删除课程 | POST | `/api/course/delete` |
| 12. 课程管理 | 课程详情 | POST | `/api/course/detail` |
| 12. 课程管理 | 课程分页 | POST | `/api/course/page` |
| 12. 课程管理 | 保存课程 | POST | `/api/course/save` |
| 12. 课程管理 | 修改课程 | POST | `/api/course/update` |
| 13. 课程章节管理 | 删除课程章节 | POST | `/api/courseChapter/delete` |
| 13. 课程章节管理 | 课程章节详情 | GET | `/api/courseChapter/detail` |
| 13. 课程章节管理 | 课程章节列表 | POST | `/api/courseChapter/list` |
| 13. 课程章节管理 | 保存课程章节 | POST | `/api/courseChapter/save` |
| 13. 课程章节管理 | 修改课程章节 | POST | `/api/courseChapter/update` |
| 14. 课程章节留言管理 | 获取课程章节留言分页 | POST | `/api/courseChapterMessage/page` |
| 14. 课程章节留言管理 | 保存课程章节留言 | POST | `/api/courseChapterMessage/save` |

---

## 接口详情


### 课程分类管理

#### 删除课程分类
- **方法**: POST
- **路径**: `/api/courseClass/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 课程分类分页
- **方法**: POST
- **路径**: `/api/courseClass/page`
- **请求体**: `id`:int64, `idNot`:int64, `name`:string, `nameLike`:string, `status`:int, `page`:Page
- **响应**: `PageResultCourseClass`

#### 保存课程分类
- **方法**: POST
- **路径**: `/api/courseClass/save`
- **请求体**: `name*`:string
- **响应**: `bool`

#### 修改课程分类
- **方法**: POST
- **路径**: `/api/courseClass/update`
- **请求体**: `id*`:int64, `name`:string, `status`:int
- **响应**: `bool`

### 课程标签管理

#### 删除课程标签
- **方法**: POST
- **路径**: `/api/courseTag/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 课程标签分页
- **方法**: POST
- **路径**: `/api/courseTag/page`
- **请求体**: `id`:int64, `idNot`:int64, `name`:string, `nameLike`:string, `status`:int, `page`:Page
- **响应**: `PageResultCourseTag`

#### 保存课程标签
- **方法**: POST
- **路径**: `/api/courseTag/save`
- **请求体**: `name*`:string
- **响应**: `bool`

#### 修改课程标签
- **方法**: POST
- **路径**: `/api/courseTag/update`
- **请求体**: `id*`:int64, `name`:string, `status`:int
- **响应**: `bool`


### 课程管理

#### 删除课程
- **方法**: POST
- **路径**: `/api/course/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 课程详情
- **方法**: POST
- **路径**: `/api/course/detail`
- **请求体**: `id*`:int64
- **响应**: `CourseDetail`

#### 课程分页
- **方法**: POST
- **路径**: `/api/course/page`
- **请求体**: `id`:int64, `idNot`:int64, `titleLike`:string, `courseClassId`:int64, `status`:int, `page`:Page
- **响应**: `PageResultCourse`

#### 保存课程
- **方法**: POST
- **路径**: `/api/course/save`
- **请求体**: `title*`:string, `courseClassId*`:int64, `teacherId*`:int64, `priceType`:int, `price`:number, `summary`:string, `coverAttachmentId`:int64, `caseDetail`:string, `isPublic`:int, `isOriginal`:int, `status*`:int, `tags`:[]integer, `attachments`:[]integer
- **响应**: `bool`

#### 修改课程
- **方法**: POST
- **路径**: `/api/course/update`
- **请求体**: `id*`:int64, `title`:string, `courseClassId`:int64, `teacherId`:int64, `priceType`:int, `price`:number, `summary`:string, `coverAttachmentId`:int64, `caseDetail`:string, `isPublic`:int, `isOriginal`:int, `status`:int, `tags`:[]integer, `attachments`:[]integer
- **响应**: `bool`

### 课程章节管理

#### 删除课程章节
- **方法**: POST
- **路径**: `/api/courseChapter/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 课程章节详情
- **方法**: GET
- **路径**: `/api/courseChapter/detail`
- **查询参数**: `id*`:int64
- **响应**: `CourseChapterDetail`

#### 课程章节列表
- **方法**: POST
- **路径**: `/api/courseChapter/list`
- **请求体**: `id`:int64, `courseId`:int64, `titleLike`:string, `parentId`:int64, `isFree`:int
- **响应**: `CourseChapterTreeNode`

#### 保存课程章节
- **方法**: POST
- **路径**: `/api/courseChapter/save`
- **请求体**: `courseId*`:int64, `title*`:string, `parentId*`:int64, `isFree*`:int, `videoAttachmentId`:int64, `videoLength`:int, `content`:string, `attachments`:[]integer
- **响应**: `bool`

#### 修改课程章节
- **方法**: POST
- **路径**: `/api/courseChapter/update`
- **请求体**: `id*`:int64, `courseId`:int64, `title`:string, `parentId`:int64, `isFree`:int, `videoAttachmentId`:int64, `videoLength`:int, `content`:string, `attachments`:[]integer
- **响应**: `bool`

### 课程章节留言管理

#### 获取课程章节留言分页
- **方法**: POST
- **路径**: `/api/courseChapterMessage/page`
- **请求体**: `id`:int64, `courseChapterId`:int64, `replyId`:int64, `current`:int, `size`:int
- **响应**: `PageResultCourseChapterMessageReply`

#### 保存课程章节留言
- **方法**: POST
- **路径**: `/api/courseChapterMessage/save`
- **请求体**: `courseChapterId*`:int64, `replyId`:int64, `content`:string
- **响应**: `bool`

### Hello

#### You first hello api
- **方法**: GET
- **路径**: `/api/hello`

---

## 核心数据模型

### Article

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | id |
| `title` | string | 标题 |
| `summary` | string | 简介 |
| `content` | string | 内容 |
| `articleClassId` | string | 文章类型id |
| `isPublic` | int | 是否公开，字典值：NORMAL::BOOL |
| `isOriginal` | int | 是否原创，字典值：NORMAL::BOOL |
| `coverAttachmentId` | string | 封面，附件id |
| `createUserId` | string | 创建用户id |
| `createTime` | string | 创建时间 |
| `status` | int | 状态，字典值：ARTICLE::STATUS |
| `visitCount` | string | 浏览量 |
| `articleTags` | []string | 文章标签 |
| `createUserName` | string | 创建用户名称 |

### ArticleClass

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | id |
| `name` | string | 分类名称 |
| `status` | int | 状态 |

### ArticleEs

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | id |
| `title` | string | 标题 |
| `isOriginal` | int | 是否原创 |
| `isPublic` | int | 是否公开 |
| `articleTags` | []string | 标签集合 |
| `visitCount` | string | 访问次数 |
| `coverAttachmentId` | string | 封面附件id |
| `createTime` | string | 创建时间 |
| `createUserId` | string | 作者id |
| `createUserName` | string | 作者名称 |
| `contentPlain` | string | 提要内容 |

### ArticleMessageReply

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | int64 | id |
| `articleId` | int64 | 文章id |
| `replyMessageId` | int64 | 回复的留言id |
| `content` | string | 内容 |
| `createUserId` | int64 | 留言者id |
| `createUserName` | string | 留言者名称 |
| `createTime` | string | 创建时间 |
| `replies` | []ArticleMessageReply | 留言回复 |

### ArticleTag

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | ID |
| `name` | string | 标签名称 |
| `status` | int | 状态 |

### AttachmentUploadResult

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | id |
| `storePosition` | string | 存储位置 |

### Course

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | id |
| `title` | string | 课程标题 |
| `courseClassId` | string | 课程分类ID |
| `teacherId` | string | 讲师ID |
| `priceType` | int | 收费类型 |
| `price` | number | 价格 |
| `summary` | string | 简介 |
| `coverAttachmentId` | string | 封面附件ID |
| `isPublic` | int | 是否公开 |
| `isOriginal` | int | 是否原创 |
| `createTime` | string | 创建时间 |
| `status` | int | 状态 |

### CourseChapterDetail

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | id |
| `title` | string | 章节标题 |
| `parentId` | string | 父级id |
| `isFree` | int | 是否免费，字典值：NORMAL::BOOL |
| `createTime` | string | 创建时间 |
| `videoAttachmentId` | string | 视频附件id |
| `videoLength` | int | 视频时长，单位秒 |
| `content` | string | 图文内容 |
| `attachmentIds` | []string | 附件ID列表 |

### CourseChapterMessageReply

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | id |
| `courseChapterId` | string | 课程章节id |
| `replyId` | string | 回复的留言id |
| `content` | string | 内容 |
| `createUserId` | string | 留言者id |
| `createUserName` | string | 留言者名称 |
| `createTime` | string | 创建时间 |
| `replies` | []CourseChapterMessageReply | 留言回复 |

### CourseClass

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | id |
| `name` | string | 分类名称 |
| `status` | int | 状态 |

### CourseDetail

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | int64 | id |
| `title` | string | 课程标题 |
| `courseClassId` | int64 | 课程分类ID |
| `teacherId` | int64 | 讲师ID |
| `priceType` | int | 收费类型 |
| `price` | number | 价格 |
| `summary` | string | 简介 |
| `caseDetail` | string | 案情详情 |
| `coverAttachmentId` | int64 | 封面附件ID |
| `isPublic` | int | 是否公开 |
| `isOriginal` | int | 是否原创 |
| `createTime` | string | 创建时间 |
| `status` | int | 状态 |
| `tagIds` | []integer | 标签ID列表 |
| `attachmentIds` | []integer | 附件ID列表 |

### CourseTag

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | int64 | id |
| `name` | string | 标签名称 |
| `status` | int | 状态 |

### DepartmentTree

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | - |
| `code` | string | - |
| `name` | string | - |
| `status` | int | - |
| `statusDesc` | string | - |
| `children` | []DepartmentTree | - |

### MenuInfo

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | - |
| `menuType` | int | - |
| `menuName` | string | - |
| `routeName` | string | - |
| `routePath` | string | - |
| `pathParam` | string | - |
| `component` | string | - |
| `layout` | string | - |
| `page` | string | - |
| `i18nKey` | string | - |
| `icon` | string | - |
| `iconType` | int | - |
| `parentId` | int64 | - |
| `status` | int | - |
| `keepAlive` | int | - |
| `constant` | int | - |
| `order` | int | - |
| `href` | string | - |
| `hideInMenu` | int | - |
| `activeMenu` | string | - |
| `multiTab` | int | - |
| `fixedIndexInTab` | string | - |
| `query` | string | - |
| `buttons` | string | - |

### MenuTree

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | - |
| `menuType` | int | - |
| `menuName` | string | - |
| `routeName` | string | - |
| `routePath` | string | - |
| `pathParam` | string | - |
| `component` | string | - |
| `layout` | string | - |
| `page` | string | - |
| `i18nKey` | string | - |
| `icon` | string | - |
| `iconType` | int | - |
| `parentId` | int64 | - |
| `status` | int | - |
| `keepAlive` | int | - |
| `constant` | int | - |
| `order` | int | - |
| `href` | string | - |
| `hideInMenu` | int | - |
| `activeMenu` | string | - |
| `multiTab` | int | - |
| `fixedIndexInTab` | string | - |
| `query` | string | - |
| `buttons` | string | - |
| `children` | []MenuTree | - |

### PageResultArticleClass

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []ArticleClass | 数据列表 |

### PageResultArticleEs

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []ArticleEs | 数据列表 |

### PageResultArticleMessageReply

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []ArticleMessageReply | 数据列表 |

### PageResultArticleTag

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []ArticleTag | 数据列表 |

### PageResultCourse

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []Course | 数据列表 |

### PageResultCourseChapterMessageReply

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []CourseChapterMessageReply | 数据列表 |

### PageResultCourseClass

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []CourseClass | 数据列表 |

### PageResultCourseTag

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []CourseTag | 数据列表 |

### PageResultMenuInfo

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []MenuInfo | 数据列表 |

### PageResultMenuTree

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []MenuTree | 数据列表 |

### PageResultRole

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []Role | 数据列表 |

### PageResultUser

| 字段 | 类型 | 描述 |
|------|------|------|
| `current` | int | 当前页码 |
| `size` | int | 每页条数 |
| `total` | int | 总记录数 |
| `totalPage` | int | 总页数 |
| `records` | []User | 数据列表 |

### Role

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | id |
| `name` | string | 角色名称 |
| `code` | string | 角色编号 |
| `status` | int | 状态 |
| `menus` | []string | 菜单集合 |

### User

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | - |
| `userName` | string | - |
| `nickName` | string | - |
| `userGender` | int | - |
| `userPhone` | string | - |
| `userEmail` | string | - |
| `departmentId` | int64 | - |
| `status` | int | - |
| `createTime` | int64 | - |
| `userRoles` | []string | - |

### UserInfo

| 字段 | 类型 | 描述 |
|------|------|------|
| `userId` | string | - |
| `userName` | string | - |
| `roles` | githubcomgogfgfv2containergsetStrSet |  |
| `buttons` | githubcomgogfgfv2containergsetStrSet |  |

### UserLogin

| 字段 | 类型 | 描述 |
|------|------|------|
| `token` | string | - |
| `refreshToken` | string | - |

---

## 使用说明

1. 带有 `*` 标记的参数为必填参数
2. 所有 POST 请求使用 `application/json` 格式
3. 分页接口通常需要提供 `current`(当前页) 和 `size`(每页条数) 参数
4. 删除接口通常接收 `ids` 数组参数
5. 响应格式统一包含 `code`, `message`, `data` 字段(data 内容为上述响应类型)
