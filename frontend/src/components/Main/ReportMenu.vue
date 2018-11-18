<template>
    <el-menu 
      default-active=/
      router
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      @select="handleSelect"
      >
      <el-menu-item index="reportedit">
        <i class="el-icon-edit"></i>
        <span slot="title">写报告</span>
      </el-menu-item>
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

  }
</script>

<style>

</style>