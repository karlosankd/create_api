# CMS 平台 API 参考文档 (AI 版)

本文档提供 API 接口的精简描述，适合 AI 助手快速理解和使用。

## API 快速索引

| 模块 | 接口 | 方法 | 路径 |
|------|------|------|------|
| 01. 用户管理 | 获取当前用户信息 | GET | `/api/user/current` |
| 01. 用户管理 | 当前用户菜单树 | GET | `/api/user/currentMenuTree` |
| 01. 用户管理 | 删除用户 | POST | `/api/user/delete` |
| 01. 用户管理 | 用户登录验证 | POST | `/api/user/login` |
| 01. 用户管理 | 分页查询用户 | POST | `/api/user/page` |
| 01. 用户管理 | 保存用户 | POST | `/api/user/save` |
| 01. 用户管理 | 修改用户 | POST | `/api/user/update` |
| 02. 部门管理 | 保存部门 | POST | `/api/department/save` |
| 02. 部门管理 | 获取部门树结构 | POST | `/api/department/tree` |
| 02. 部门管理 | 更新部门 | POST | `/api/department/update` |
| 03. 菜单管理 | 删除菜单 | POST | `/api/menu/delete` |
| 03. 菜单管理 | 菜单分页 | POST | `/api/menu/page` |
| 03. 菜单管理 | 保存菜单 | POST | `/api/menu/save` |
| 03. 菜单管理 | 顶级菜单的分页树形结构 | POST | `/api/menu/topPageTree` |
| 03. 菜单管理 | 菜单树 | GET | `/api/menu/tree` |
| 03. 菜单管理 | 更新菜单 | POST | `/api/menu/update` |
| 04. 角色管理 | 获取角色拥有的文章类型列表 | POST | `/api/role/articleClassList` |
| 04. 角色管理 | 角色文章类型关系保存 | POST | `/api/role/articleClassSave` |
| 04. 角色管理 | 删除角色 | POST | `/api/role/delete` |
| 04. 角色管理 | 角色分页 | POST | `/api/role/page` |
| 04. 角色管理 | 角色菜单关系保存 | POST | `/api/role/roleMenus` |
| 04. 角色管理 | 保存角色 | POST | `/api/role/save` |
| 04. 角色管理 | 修改角色 | POST | `/api/role/update` |
| 05. 文章分类管理 | 删除文章分类 | POST | `/api/articleClass/delete` |
| 05. 文章分类管理 | 文章分类分页 | POST | `/api/articleClass/page` |
| 05. 文章分类管理 | 保存文章分类 | POST | `/api/articleClass/save` |
| 05. 文章分类管理 | 修改文章分类 | POST | `/api/articleClass/update` |
| 06. 文章管理 | 删除文章 | POST | `/api/article/delete` |
| 06. 文章管理 | 通过ID获取文章详情 | GET | `/api/article/detail` |
| 06. 文章管理 | 分页查询文章 | POST | `/api/article/page` |
| 06. 文章管理 | 文章保存 | POST | `/api/article/save` |
| 06. 文章管理 | 修改文章 | POST | `/api/article/update` |
| 06. 文章管理 | 文章访问次数递增 | GET | `/api/article/visitIncrement` |
| 07. 附件管理 | 加载附件 | GET | `/api/attachment/load` |
| 07. 附件管理 | 上传附件 | POST | `/api/attachment/upload` |
| 08. 留言管理 | 获取留言分页 | POST | `/api/articleMessage/page` |
| 08. 留言管理 | 保存留言 | POST | `/api/articleMessage/save` |
| 09. 课程分类管理 | 删除课程分类 | POST | `/api/courseClass/delete` |
| 09. 课程分类管理 | 课程分类分页 | POST | `/api/courseClass/page` |
| 09. 课程分类管理 | 保存课程分类 | POST | `/api/courseClass/save` |
| 09. 课程分类管理 | 修改课程分类 | POST | `/api/courseClass/update` |
| 10. 课程标签管理 | 删除课程标签 | POST | `/api/courseTag/delete` |
| 10. 课程标签管理 | 课程标签分页 | POST | `/api/courseTag/page` |
| 10. 课程标签管理 | 保存课程标签 | POST | `/api/courseTag/save` |
| 10. 课程标签管理 | 修改课程标签 | POST | `/api/courseTag/update` |
| 11. 文章标签管理 | 删除文章标签 | POST | `/api/articleTag/delete` |
| 11. 文章标签管理 | 文章标签分页 | POST | `/api/articleTag/page` |
| 11. 文章标签管理 | 保存文章标签 | POST | `/api/articleTag/save` |
| 11. 文章标签管理 | 修改文章标签 | POST | `/api/articleTag/update` |
| 12. 课程管理 | 删除课程 | POST | `/api/course/delete` |
| 12. 课程管理 | 课程详情 | GET | `/api/course/detail` |
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
| Hello | You first hello api | GET | `/api/hello` |

---

## 接口详情

### 用户管理

#### 获取当前用户信息
- **方法**: GET
- **路径**: `/api/user/current`
- **响应**: `UserInfo`

#### 当前用户菜单树
- **方法**: GET
- **路径**: `/api/user/currentMenuTree`
- **响应**: `MenuTree`

#### 删除用户
- **方法**: POST
- **路径**: `/api/user/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 用户登录验证
- **方法**: POST
- **路径**: `/api/user/login`
- **请求体**: `userName*`:string, `password*`:string
- **响应**: `UserLogin`

#### 分页查询用户
- **方法**: POST
- **路径**: `/api/user/page`
- **请求体**: `userName`:string, `nickName`:string, `departmentId`:int64, `status`:int, `page`:Page
- **响应**: `PageResultUser`

#### 保存用户
- **方法**: POST
- **路径**: `/api/user/save`
- **请求体**: `userName*`:string, `nickName*`:string, `password*`:string, `departmentId`:int64, `userGender`:int, `userPhone`:string, `userEmail`:string, `userRoles`:[]integer
- **响应**: `bool`

#### 修改用户
- **方法**: POST
- **路径**: `/api/user/update`
- **请求体**: `id*`:int64, `userName`:string, `nickName`:string, `password`:string, `departmentId`:int64, `status`:int, `userGender`:int, `userPhone`:string, `userEmail`:string, `userRoles`:[]integer
- **响应**: `bool`

### 部门管理

#### 保存部门
- **方法**: POST
- **路径**: `/api/department/save`
- **请求体**: `code*`:string, `name*`:string, `pid*`:int64
- **响应**: `bool`

#### 获取部门树结构
- **方法**: POST
- **路径**: `/api/department/tree`
- **查询参数**: `pid`:int64
- **响应**: `*voDepartmentTree`

#### 更新部门
- **方法**: POST
- **路径**: `/api/department/update`
- **请求体**: `id*`:int64, `name`:string, `pid`:int64, `status`:int
- **响应**: `bool`

### 菜单管理

#### 删除菜单
- **方法**: POST
- **路径**: `/api/menu/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 菜单分页
- **方法**: POST
- **路径**: `/api/menu/page`
- **请求体**: `id`:int64, `menuType`:int, `menuName`:string, `parentId`:int64, `status`:int, `statusNot`:int, `page`:Page
- **响应**: `PageResultMenuInfo`

#### 保存菜单
- **方法**: POST
- **路径**: `/api/menu/save`
- **请求体**: `menuType*`:int, `menuName*`:string, `routeName`:string, `routePath`:string, `pathParam`:string, `component`:string, `layout`:string, `page`:string, `i18nKey`:string, `icon`:string, `iconType`:int, `parentId`:int64, `status`:int, `keepAlive`:int, `constant`:int, `order`:int, `href`:string, `hideInMenu`:int, `activeMenu`:string, `multiTab`:int, `fixedIndexInTab`:string, `query`:string, `buttons`:string
- **响应**: `bool`

#### 顶级菜单的分页树形结构
- **方法**: POST
- **路径**: `/api/menu/topPageTree`
- **请求体**: `page`:Page
- **响应**: `PageResultMenuTree`

#### 菜单树
- **方法**: GET
- **路径**: `/api/menu/tree`
- **查询参数**: `pid`:int64
- **响应**: `MenuTree`

#### 更新菜单
- **方法**: POST
- **路径**: `/api/menu/update`
- **请求体**: `id*`:int64, `menuType`:int, `menuName`:string, `routePath`:string, `pathParam`:string, `component`:string, `layout`:string, `page`:string, `i18NKey`:string, `icon`:string, `iconType`:int, `parentId`:int64, `status`:int, `keepAlive`:int, `constant`:int, `order`:int, `href`:string, `hideInMenu`:int, `activeMenu`:string, `multiTab`:int, `fixedIndexInTab`:string, `query`:string, `buttons`:string
- **响应**: `bool`

### 角色管理

#### 获取角色拥有的文章类型列表
- **方法**: POST
- **路径**: `/api/role/articleClassList`
- **请求体**: `roleId*`:int64
- **响应**: `RoleArticleClassInfo`

#### 角色文章类型关系保存
- **方法**: POST
- **路径**: `/api/role/articleClassSave`
- **请求体**: `roleId*`:int64, `articleClassIds*`:[]integer
- **响应**: `bool`

#### 删除角色
- **方法**: POST
- **路径**: `/api/role/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 角色分页
- **方法**: POST
- **路径**: `/api/role/page`
- **请求体**: `id`:int64, `code`:string, `name`:string, `status`:int, `statusNot`:int, `page`:Page
- **响应**: `PageResultRole`

#### 角色菜单关系保存
- **方法**: POST
- **路径**: `/api/role/roleMenus`
- **请求体**: `roleId*`:int64, `menuIds*`:[]integer
- **响应**: `bool`

#### 保存角色
- **方法**: POST
- **路径**: `/api/role/save`
- **请求体**: `code*`:string, `name*`:string, `desc`:string, `status`:int
- **响应**: `bool`

#### 修改角色
- **方法**: POST
- **路径**: `/api/role/update`
- **请求体**: `id*`:int64, `code`:string, `name`:string, `desc`:string, `status`:int
- **响应**: `bool`

### 文章分类管理

#### 删除文章分类
- **方法**: POST
- **路径**: `/api/articleClass/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 文章分类分页
- **方法**: POST
- **路径**: `/api/articleClass/page`
- **请求体**: `id`:int64, `idNot`:int64, `name`:string, `nameLike`:string, `status`:int, `page`:Page
- **响应**: `PageResultArticleClass`

#### 保存文章分类
- **方法**: POST
- **路径**: `/api/articleClass/save`
- **请求体**: `name*`:string
- **响应**: `bool`

#### 修改文章分类
- **方法**: POST
- **路径**: `/api/articleClass/update`
- **请求体**: `id*`:int64, `name`:string, `status`:int
- **响应**: `bool`

### 文章管理

#### 删除文章
- **方法**: POST
- **路径**: `/api/article/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 通过ID获取文章详情
- **方法**: GET
- **路径**: `/api/article/detail`
- **查询参数**: `id*`:int64
- **响应**: `Article`

#### 分页查询文章
- **方法**: POST
- **路径**: `/api/article/page`
- **请求体**: `isPublic`:int, `articleClassId`:string, `articleTags`:[]string, `keyword`:string, `Page`:Page
- **响应**: `PageResultArticleEs`

#### 文章保存
- **方法**: POST
- **路径**: `/api/article/save`
- **请求体**: `title*`:string, `summary`:string, `content*`:string, `isPublic*`:int, `articleClassId*`:int64, `articleTags`:[]integer, `isOriginal*`:int, `coverAttachmentId`:int64, `status*`:int
- **响应**: `bool`

#### 修改文章
- **方法**: POST
- **路径**: `/api/article/update`
- **请求体**: `id*`:int64, `title`:string, `summary`:string, `content`:string, `isPublic`:int, `articleClassId`:int64, `articleTags`:[]integer, `isOriginal`:int, `coverAttachmentId`:int64, `status*`:int
- **响应**: `bool`

#### 文章访问次数递增
- **方法**: GET
- **路径**: `/api/article/visitIncrement`
- **查询参数**: `id*`:int64
- **响应**: `bool`

### 附件管理

#### 加载附件
- **方法**: GET
- **路径**: `/api/attachment/load`
- **查询参数**: `id*`:int64
- **响应**: `bool`

#### 上传附件
- **方法**: POST
- **路径**: `/api/attachment/upload`
- **请求体**: `file*`:file
- **响应**: `AttachmentUploadResult`

### 留言管理

#### 获取留言分页
- **方法**: POST
- **路径**: `/api/articleMessage/page`
- **请求体**: `id`:int64, `articleId`:int64, `replyMessageId`:int64, `replyMessageIds`:[]integer, `current`:int, `size`:int
- **响应**: `PageResultArticleMessageReply`

#### 保存留言
- **方法**: POST
- **路径**: `/api/articleMessage/save`
- **请求体**: `articleId*`:int64, `replyMessageId`:int64, `content*`:string
- **响应**: `bool`

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

### 文章标签管理

#### 删除文章标签
- **方法**: POST
- **路径**: `/api/articleTag/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 文章标签分页
- **方法**: POST
- **路径**: `/api/articleTag/page`
- **请求体**: `id`:int64, `idNot`:int64, `name`:string, `nameLike`:string, `status`:int, `page`:Page
- **响应**: `PageResultArticleTag`

#### 保存文章标签
- **方法**: POST
- **路径**: `/api/articleTag/save`
- **请求体**: `name*`:string
- **响应**: `bool`

#### 修改文章标签
- **方法**: POST
- **路径**: `/api/articleTag/update`
- **请求体**: `id*`:int64, `name`:string, `status`:int
- **响应**: `bool`

### 课程管理

#### 删除课程
- **方法**: POST
- **路径**: `/api/course/delete`
- **请求体**: `ids*`:[]integer
- **响应**: `bool`

#### 课程详情
- **方法**: GET
- **路径**: `/api/course/detail`
- **查询参数**: `id*`:int64
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
- **请求体**: `courseId*`:int64, `type*`:int, `title*`:string, `parentId*`:int64, `isFree*`:int, `videoAttachmentId`:int64, `videoLength`:int, `content`:string, `attachments`:[]integer
- **响应**: `bool`

#### 修改课程章节
- **方法**: POST
- **路径**: `/api/courseChapter/update`
- **请求体**: `id*`:int64, `type`:int, `courseId`:int64, `title`:string, `parentId`:int64, `isFree`:int, `videoAttachmentId`:int64, `videoLength`:int, `content`:string, `attachments`:[]integer
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
| `teacherName` | string | 讲师名称 |
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
| `type` | int | 章节类型，字典值：COURSE_CHAPTER::TYPE |
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
| `teacherName` | string | 讲师名称 |
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
