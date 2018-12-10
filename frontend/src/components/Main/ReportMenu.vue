<template>
    <el-menu 
      :default-active="$route.path"
      router
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      :default-openeds="openeds"
      >
      <el-submenu index="reportedit">
        <template  slot="title">
          <i class="el-icon-edit"></i>
          <span>写报告</span>
        </template>
        <el-menu-item index="pc_report">PC端</el-menu-item>
        <el-menu-item index="phone_report">移动端</el-menu-item>
      </el-submenu>
      <el-menu-item index="/">
        <i class="el-icon-view"></i>
        <span slot="title">报告列表</span>
      </el-menu-item>
      <el-menu-item index="buglist">
        <i class="el-icon-info"></i>
        <span slot="title">bug列表</span>
      </el-menu-item>
    </el-menu>
</template>

<script>
  export default {
    data() {
      return {
        openeds: ["reportedit"],
        uniqueOpened: false
      }
    }
}
</script>

<style>
</style>