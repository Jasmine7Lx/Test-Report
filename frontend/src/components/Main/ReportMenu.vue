<template>
    <el-menu
      :default-active="$route.path"
      router
      background-color="#fff"
      text-color="#303133"
      active-text-color="#409eff"
      class="sidebar"
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
        <span slot="title">Bug统计</span>
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

<style scoped >
.sidebar {
  border: none;
}
</style>
