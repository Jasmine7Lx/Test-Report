<template>
    <el-menu 
      :default-active="$route.path"
      router
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      >
      <!-- <el-submenu index="reportedit">
        <template  slot="title">
          <i class="el-icon-edit"></i>
          <span>写报告</span>
        </template>
        <el-menu-item index="pc_report">PC端</el-menu-item>
        <el-menu-item index="phone_report">移动端</el-menu-item>
      </el-submenu> -->
      <el-menu-item index="/report/edit">
        <i class="el-icon-edit"></i>
        <span slot="title">新增报告</span>
      </el-menu-item>
      <el-menu-item index="/">
        <i class="el-icon-view"></i>
        <span slot="title">报告列表</span>
      </el-menu-item>
      <el-menu-item index="/demand/list">
        <i class="el-icon-document"></i>
        <span slot="title">需求列表</span>
      </el-menu-item>
      <el-menu-item index="/bug/list">
        <i class="el-icon-info"></i>
        <span slot="title">bug列表</span>
      </el-menu-item>
    </el-menu>
</template>

<script>
  export default {
    data() {
      return {
      }
    }
}
</script>

<style>
</style>