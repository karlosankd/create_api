# API 接口文档

> 本文档由 Swagger JSON 自动生成

## 目录

- [01. 用户管理](#01-用户管理)
- [02. 部门管理](#02-部门管理)
- [03. 菜单管理](#03-菜单管理)
- [04. 角色管理](#04-角色管理)
- [05. 文章分类管理](#05-文章分类管理)
- [06. 文章管理](#06-文章管理)
- [07. 附件管理](#07-附件管理)
- [08. 留言管理](#08-留言管理)
- [09. 课程分类管理](#09-课程分类管理)
- [10. 课程标签管理](#10-课程标签管理)
- [11. 文章标签管理](#11-文章标签管理)
- [12. 课程管理](#12-课程管理)
- [13. 课程章节管理](#13-课程章节管理)
- [14. 课程章节留言管理](#14-课程章节留言管理)
- [Hello](#hello)

---

## 01. 用户管理

### 4. 获取当前用户信息

**GET** `/api/user/current`

**响应:**

- `userId` (string)
- `userName` (string)
- `roles` (githubcomgogfgfv2containergsetStrSet)
- `buttons` (githubcomgogfgfv2containergsetStrSet)

---

### 7. 当前用户菜单树

**GET** `/api/user/currentMenuTree`

---

### 6. 删除用户

**POST** `/api/user/delete`

**请求体:**

- `ids` ([]integer) *(必填)*

---

### 1. 用户登录验证

**POST** `/api/user/login`

**请求体:**

- `userName` (string): 用户名 *(必填)*
- `password` (string): 密码 *(必填)*

**响应:**

- `token` (string)
- `refreshToken` (string)

---

### 2. 分页查询用户

**POST** `/api/user/page`

**请求体:**

- `userName` (string)
- `nickName` (string)
- `departmentId` (int64)
- `status` (int)
- `page` (Page)
  - `current` (int): 当前页
  - `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]User): 数据列表

---

### 3. 保存用户

**POST** `/api/user/save`

**请求体:**

- `userName` (string) *(必填)*
- `nickName` (string) *(必填)*
- `password` (string) *(必填)*
- `departmentId` (int64)
- `userGender` (int)
- `userPhone` (string)
- `userEmail` (string)
- `userRoles` ([]integer)

---

### 5. 修改用户

**POST** `/api/user/update`

**请求体:**

- `id` (int64) *(必填)*
- `userName` (string)
- `nickName` (string)
- `password` (string)
- `departmentId` (int64)
- `status` (int)
- `userGender` (int)
- `userPhone` (string)
- `userEmail` (string)
- `userRoles` ([]integer)

---

## 02. 部门管理

### 2. 保存部门

**POST** `/api/department/save`

**请求体:**

- `code` (string) *(必填)*
- `name` (string) *(必填)*
- `pid` (int64) *(必填)*

---

### 1. 获取部门树结构

**POST** `/api/department/tree`

**查询参数:**

- `pid` (int64)

---

### 3. 更新部门

**POST** `/api/department/update`

**请求体:**

- `id` (int64) *(必填)*
- `name` (string)
- `pid` (int64)
- `status` (int)

---

## 03. 菜单管理

### 6. 删除菜单

**POST** `/api/menu/delete`

**请求体:**

- `ids` ([]integer) *(必填)*

---

### 4. 菜单分页

**POST** `/api/menu/page`

**请求体:**

- `id` (int64)
- `menuType` (int)
- `menuName` (string)
- `parentId` (int64)
- `status` (int)
- `statusNot` (int)
- `page` (Page)
  - `current` (int): 当前页
  - `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]MenuInfo): 数据列表

---

### 1. 保存菜单

**POST** `/api/menu/save`

**请求体:**

- `menuType` (int) *(必填)*
- `menuName` (string) *(必填)*
- `routeName` (string)
- `routePath` (string)
- `pathParam` (string)
- `component` (string)
- `layout` (string)
- `page` (string)
- `i18nKey` (string)
- `icon` (string)
- `iconType` (int)
- `parentId` (int64)
- `status` (int)
- `keepAlive` (int)
- `constant` (int)
- `order` (int)
- `href` (string)
- `hideInMenu` (int)
- `activeMenu` (string)
- `multiTab` (int)
- `fixedIndexInTab` (string)
- `query` (string)
- `buttons` (string)

---

### 3. 顶级菜单的分页树形结构

**POST** `/api/menu/topPageTree`

**请求体:**

- `page` (Page)
  - `current` (int): 当前页
  - `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]MenuTree): 数据列表

---

### 2. 菜单树

**GET** `/api/menu/tree`

**查询参数:**

- `pid` (int64)

---

### 5. 更新菜单

**POST** `/api/menu/update`

**请求体:**

- `id` (int64) *(必填)*
- `menuType` (int)
- `menuName` (string)
- `routePath` (string)
- `pathParam` (string)
- `component` (string)
- `layout` (string)
- `page` (string)
- `i18NKey` (string)
- `icon` (string)
- `iconType` (int)
- `parentId` (int64)
- `status` (int)
- `keepAlive` (int)
- `constant` (int)
- `order` (int)
- `href` (string)
- `hideInMenu` (int)
- `activeMenu` (string)
- `multiTab` (int)
- `fixedIndexInTab` (string)
- `query` (string)
- `buttons` (string)

---

## 04. 角色管理

### 7. 获取角色拥有的文章类型列表

**POST** `/api/role/articleClassList`

**请求体:**

- `roleId` (int64) *(必填)*

---

### 6. 角色文章类型关系保存

**POST** `/api/role/articleClassSave`

**请求体:**

- `roleId` (int64) *(必填)*
- `articleClassIds` ([]integer) *(必填)*

---

### 4. 删除角色

**POST** `/api/role/delete`

**请求体:**

- `ids` ([]integer) *(必填)*

---

### 2. 角色分页

**POST** `/api/role/page`

**请求体:**

- `id` (int64): id
- `code` (string): 部门编号
- `name` (string): 部门名称
- `status` (int): 状态，字典值：DEPARTMENT::STATUS
- `statusNot` (int): 排除状态，字典值：DEPARTMENT::STATUS
- `page` (Page): 分页
  - `current` (int): 当前页
  - `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]Role): 数据列表

---

### 5. 角色菜单关系保存

**POST** `/api/role/roleMenus`

**请求体:**

- `roleId` (int64) *(必填)*
- `menuIds` ([]integer) *(必填)*

---

### 1. 保存角色

**POST** `/api/role/save`

**请求体:**

- `code` (string) *(必填)*
- `name` (string) *(必填)*
- `desc` (string)
- `status` (int)

---

### 3. 修改角色

**POST** `/api/role/update`

**请求体:**

- `id` (int64) *(必填)*
- `code` (string)
- `name` (string)
- `desc` (string)
- `status` (int)

---

## 05. 文章分类管理

### 4. 删除文章分类

**POST** `/api/articleClass/delete`

**请求体:**

- `ids` ([]integer): 分类id集合 *(必填)*

---

### 2. 文章分类分页

**POST** `/api/articleClass/page`

**请求体:**

- `id` (int64): id
- `idNot` (int64): 排除的id
- `name` (string): 分类名称
- `nameLike` (string): 分类名称模糊条件
- `status` (int): 状态
- `page` (Page): 分页
  - `current` (int): 当前页
  - `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]ArticleClass): 数据列表

---

### 1. 保存文章分类

**POST** `/api/articleClass/save`

**请求体:**

- `name` (string): 名称 *(必填)*

---

### 3. 修改文章分类

**POST** `/api/articleClass/update`

**请求体:**

- `id` (int64): id *(必填)*
- `name` (string): 名称
- `status` (int): 状态，字典值: ARTICLE_CLASS::STATUS

---

## 06. 文章管理

### 3. 删除文章

**POST** `/api/article/delete`

**请求体:**

- `ids` ([]integer) *(必填)*

---

### 6. 通过ID获取文章详情

**GET** `/api/article/detail`

**查询参数:**

- `id` (int64): 文章ID *(必填)*

**响应:**

- `id` (string): id
- `title` (string): 标题
- `summary` (string): 简介
- `content` (string): 内容
- `articleClassId` (string): 文章类型id
- `isPublic` (int): 是否公开，字典值：NORMAL::BOOL
- `isOriginal` (int): 是否原创，字典值：NORMAL::BOOL
- `coverAttachmentId` (string): 封面，附件id
- `createUserId` (string): 创建用户id
- `createTime` (string): 创建时间
- `status` (int): 状态，字典值：ARTICLE::STATUS
- `visitCount` (string): 浏览量
- `articleTags` ([]string): 文章标签
- `createUserName` (string): 创建用户名称

---

### 4. 分页查询文章

**POST** `/api/article/page`

**请求体:**

- `isPublic` (int): 是否公开
- `articleClassId` (string): 文章类型
- `articleTags` ([]string): 文章标签
- `keyword` (string): 关键字
- `Page` (Page)
  - `current` (int): 当前页
  - `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]ArticleEs): 数据列表

---

### 1. 文章保存

**POST** `/api/article/save`

**请求体:**

- `title` (string): 标题 *(必填)*
- `summary` (string): 摘要
- `content` (string): 内容 *(必填)*
- `isPublic` (int): 是否公开，字典值：NORMAL::BOOL *(必填)*
- `articleClassId` (int64): 文章类型 *(必填)*
- `articleTags` ([]integer): 文章标签
- `isOriginal` (int): 是否原创，字典值：NORMAL::BOOL *(必填)*
- `coverAttachmentId` (int64): 封面，福建ID，标识：ARTICLE::COVER
- `status` (int): 状态，字典值：ARTICLE::STATUS *(必填)*

---

### 2. 修改文章

**POST** `/api/article/update`

**请求体:**

- `id` (int64): id *(必填)*
- `title` (string): 标题
- `summary` (string): 简介
- `content` (string): 内容
- `isPublic` (int): 是否公开
- `articleClassId` (int64): 文章分类
- `articleTags` ([]integer): 文章标签
- `isOriginal` (int): 是否原创
- `coverAttachmentId` (int64): 封面附件id
- `status` (int): 状态 *(必填)*

---

### 5. 文章访问次数递增

**GET** `/api/article/visitIncrement`

**查询参数:**

- `id` (int64) *(必填)*

---

## 07. 附件管理

### 2. 加载附件

**GET** `/api/attachment/load`

**查询参数:**

- `id` (int64): 附件id *(必填)*

---

### 1. 上传附件

**POST** `/api/attachment/upload`

**请求体:**

- `file` (file): 文件 *(必填)*

**响应:**

- `id` (string): id
- `storePosition` (string): 存储位置

---

## 08. 留言管理

### 2. 获取留言分页

**POST** `/api/articleMessage/page`

**请求体:**

- `id` (int64): id
- `articleId` (int64): 文章id
- `replyMessageId` (int64): 回复的留言id
- `replyMessageIds` ([]integer): 回复的留言id集合
- `current` (int): 当前页
- `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]ArticleMessageReply): 数据列表

---

### 1. 保存留言

**POST** `/api/articleMessage/save`

**请求体:**

- `articleId` (int64): 文章id *(必填)*
- `replyMessageId` (int64): 回复留言id
- `content` (string): 内容 *(必填)*

---

## 09. 课程分类管理

### 4. 删除课程分类

**POST** `/api/courseClass/delete`

**请求体:**

- `ids` ([]integer): 分类id集合 *(必填)*

---

### 2. 课程分类分页

**POST** `/api/courseClass/page`

**请求体:**

- `id` (int64): id
- `idNot` (int64): 排除的id
- `name` (string): 分类名称
- `nameLike` (string): 分类名称模糊条件
- `status` (int): 状态
- `page` (Page): 分页
  - `current` (int): 当前页
  - `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]CourseClass): 数据列表

---

### 1. 保存课程分类

**POST** `/api/courseClass/save`

**请求体:**

- `name` (string): 名称 *(必填)*

---

### 3. 修改课程分类

**POST** `/api/courseClass/update`

**请求体:**

- `id` (int64): id *(必填)*
- `name` (string): 名称
- `status` (int): 状态，字典值: COURSE_CLASS::STATUS

---

## 10. 课程标签管理

### 4. 删除课程标签

**POST** `/api/courseTag/delete`

**请求体:**

- `ids` ([]integer): 标签id集合 *(必填)*

---

### 2. 课程标签分页

**POST** `/api/courseTag/page`

**请求体:**

- `id` (int64): id
- `idNot` (int64): 排除的id
- `name` (string): 标签名称
- `nameLike` (string): 标签名称模糊条件
- `status` (int): 状态
- `page` (Page): 分页
  - `current` (int): 当前页
  - `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]CourseTag): 数据列表

---

### 1. 保存课程标签

**POST** `/api/courseTag/save`

**请求体:**

- `name` (string): 标签名称 *(必填)*

---

### 3. 修改课程标签

**POST** `/api/courseTag/update`

**请求体:**

- `id` (int64): id *(必填)*
- `name` (string): 标签名称
- `status` (int): 状态，字典值: COURSE_TAG::STATUS

---

## 11. 文章标签管理

### 4. 删除文章标签

**POST** `/api/articleTag/delete`

**请求体:**

- `ids` ([]integer): 标签id集合 *(必填)*

---

### 2. 文章标签分页

**POST** `/api/articleTag/page`

**请求体:**

- `id` (int64): id
- `idNot` (int64): 排除的id
- `name` (string): 标签名称
- `nameLike` (string): 标签名称模糊条件
- `status` (int): 状态
- `page` (Page): 分页
  - `current` (int): 当前页
  - `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]ArticleTag): 数据列表

---

### 1. 保存文章标签

**POST** `/api/articleTag/save`

**请求体:**

- `name` (string): 标签名称 *(必填)*

---

### 3. 修改文章标签

**POST** `/api/articleTag/update`

**请求体:**

- `id` (int64): id *(必填)*
- `name` (string): 标签名称
- `status` (int): 状态，字典值: ARTICLE_TAG::STATUS

---

## 12. 课程管理

### 4. 删除课程

**POST** `/api/course/delete`

**请求体:**

- `ids` ([]integer): 课程id集合 *(必填)*

---

### 5. 课程详情

**GET** `/api/course/detail`

**查询参数:**

- `id` (int64): ID *(必填)*

**响应:**

- `id` (int64): id
- `title` (string): 课程标题
- `courseClassId` (int64): 课程分类ID
- `teacherId` (int64): 讲师ID
- `teacherName` (string): 讲师名称
- `priceType` (int): 收费类型
- `price` (number): 价格
- `summary` (string): 简介
- `caseDetail` (string): 案情详情
- `coverAttachmentId` (int64): 封面附件ID
- `isPublic` (int): 是否公开
- `isOriginal` (int): 是否原创
- `createTime` (string): 创建时间
- `status` (int): 状态
- `tagIds` ([]integer): 标签ID列表
- `attachmentIds` ([]integer): 附件ID列表

---

### 2. 课程分页

**POST** `/api/course/page`

**请求体:**

- `id` (int64): id
- `idNot` (int64): 排除的id
- `titleLike` (string): 课程标题模糊条件
- `courseClassId` (int64): 课程分类ID
- `status` (int): 状态
- `page` (Page): 分页
  - `current` (int): 当前页
  - `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]Course): 数据列表

---

### 1. 保存课程

**POST** `/api/course/save`

**请求体:**

- `title` (string): 课程标题 *(必填)*
- `courseClassId` (int64): 课程分类ID *(必填)*
- `teacherId` (int64): 讲师ID *(必填)*
- `priceType` (int): 收费类型
- `price` (number): 价格
- `summary` (string): 简介
- `coverAttachmentId` (int64): 封面附件ID
- `caseDetail` (string): 案情详情
- `isPublic` (int): 是否公开
- `isOriginal` (int): 是否原创
- `status` (int): 状态 *(必填)*
- `tags` ([]integer): 标签ID列表
- `attachments` ([]integer): 附件ID列表

---

### 3. 修改课程

**POST** `/api/course/update`

**请求体:**

- `id` (int64): ID *(必填)*
- `title` (string): 课程标题
- `courseClassId` (int64): 课程分类ID
- `teacherId` (int64): 讲师ID
- `priceType` (int): 收费类型
- `price` (number): 价格
- `summary` (string): 简介
- `coverAttachmentId` (int64): 封面附件ID
- `caseDetail` (string): 案情详情
- `isPublic` (int): 是否公开
- `isOriginal` (int): 是否原创
- `status` (int): 状态
- `tags` ([]integer): 标签ID列表
- `attachments` ([]integer): 附件ID列表

---

## 13. 课程章节管理

### 3. 删除课程章节

**POST** `/api/courseChapter/delete`

**请求体:**

- `ids` ([]integer): 课程章节id集合 *(必填)*

---

### 5. 课程章节详情

**GET** `/api/courseChapter/detail`

**查询参数:**

- `id` (int64): ID *(必填)*

**响应:**

- `id` (string): id
- `type` (int): 章节类型，字典值：COURSE_CHAPTER::TYPE
- `title` (string): 章节标题
- `parentId` (string): 父级id
- `isFree` (int): 是否免费，字典值：NORMAL::BOOL
- `createTime` (string): 创建时间
- `videoAttachmentId` (string): 视频附件id
- `videoLength` (int): 视频时长，单位秒
- `content` (string): 图文内容
- `attachmentIds` ([]string): 附件ID列表

---

### 4. 课程章节列表

**POST** `/api/courseChapter/list`

**请求体:**

- `id` (int64): id
- `courseId` (int64): 课程id
- `titleLike` (string): 章节标题模糊条件
- `parentId` (int64): 父级id
- `isFree` (int): 是否免费，字典值：NORMAL::BOOL

---

### 1. 保存课程章节

**POST** `/api/courseChapter/save`

**请求体:**

- `courseId` (int64): 课程ID *(必填)*
- `type` (int): 章节类型，字典值：COURSE_CHAPTER::TYPE *(必填)*
- `title` (string): 章节标题 *(必填)*
- `parentId` (int64): 父级id *(必填)*
- `isFree` (int): 是否免费，字典值：NORMAL::BOOL *(必填)*
- `videoAttachmentId` (int64): 视频附件id
- `videoLength` (int): 视频时长，单位秒
- `content` (string): 图文内容
- `attachments` ([]integer): 附件ID列表

---

### 2. 修改课程章节

**POST** `/api/courseChapter/update`

**请求体:**

- `id` (int64): ID *(必填)*
- `type` (int): 章节类型
- `courseId` (int64): 课程ID
- `title` (string): 章节标题
- `parentId` (int64): 父级id
- `isFree` (int): 是否免费，字典值：NORMAL::BOOL
- `videoAttachmentId` (int64): 视频附件id
- `videoLength` (int): 视频时长，单位秒
- `content` (string): 图文内容
- `attachments` ([]integer): 附件ID列表

---

## 14. 课程章节留言管理

### 2. 获取课程章节留言分页

**POST** `/api/courseChapterMessage/page`

**请求体:**

- `id` (int64): id
- `courseChapterId` (int64): 课程章节id
- `replyId` (int64): 回复的留言id
- `current` (int): 当前页
- `size` (int): 每页条数

**响应:**

- `current` (int): 当前页码
- `size` (int): 每页条数
- `total` (int): 总记录数
- `totalPage` (int): 总页数
- `records` ([]CourseChapterMessageReply): 数据列表

---

### 1. 保存课程章节留言

**POST** `/api/courseChapterMessage/save`

**请求体:**

- `courseChapterId` (int64): 课程章节id *(必填)*
- `replyId` (int64): 回复留言id
- `content` (string): 内容

---

## Hello

### You first hello api

**GET** `/api/hello`

---
