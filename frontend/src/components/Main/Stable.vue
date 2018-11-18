<template>
    <el-row>
      <el-col :span="10" >
        <div id="head-title">
          测试报告管理系统
        </div>
      </el-col>
      <el-col :span="14" id="head-name"  >
      <el-dropdown>
        <i class="el-icon-edit" style="margin-right: 10px"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>查看</el-dropdown-item>
          <el-dropdown-item>新增</el-dropdown-item>
          <el-dropdown-item>删除</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown> 
      <span> Jasmine</span>
      </el-col>
    </el-row>
</template>
