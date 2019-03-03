<template>
  <header class="header">
    <h1>测试报告管理系统</h1>
    <div class="menu">
      <el-dropdown>
        <span class="name">
          <i class="el-icon-edit" style="margin-right: 10px"></i>
          Jasmine
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>查看</el-dropdown-item>
          <el-dropdown-item>新增</el-dropdown-item>
          <el-dropdown-item>删除</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </header>
</template>

<style lang="css" scoped>
.header h1 {
  margin: 0;
  color: #fff;
  height: 60px;
  line-height: 60px;
  float: left;
}
.menu {
  float: right;
  height: 60px;
  line-height: 60px;
  color: #fff;
}
.el-icon-edit,
.name {
  color: #fff;
}
</style>


