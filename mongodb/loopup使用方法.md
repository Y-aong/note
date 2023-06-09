## 聚合查询

MongoDB 中通过 aggregate([{...}]) 方法来完成聚合查询。

比较常见的聚合查询表达式有：$sum、$max、$push、$first、$last 等。

表达式只是执行具体的操作，聚合查询的核心是管道的概念，有点类似 Linux 系统的管道，用于将当前输出的结果作为下一个命令的参数。



### $lookup

主要作用为对于同一个数据库中的集合执行左外连接，相当于sql中的子查询或者left join

对每个输入的文档，$lookup 阶段会添加一个新的数组字段，其中元素是“联接”集合中匹配出来的文档。

#### 基础语法

```json
{
    $lookip:
    {
        from: "连接的附表",
        localField: "主表外联的字段",
        foreignField: "附表关联的字段",
        as: "加入字段"
    }
}
```

#### 增强语法

```json
{
    $lookip:
    {
        from: "主表",
        let: {var1: exp1,var2:exp2},    // 可选参数，指定管道字段的变量，作为入参放到接下来的管道中，可以实现多条件级联
        pipeline: [{...}],    // 管道，要连接的集合管道，全部返回指定为空管道[]
        as: "加入字段"
    }
}
```

#### 基础语法案例