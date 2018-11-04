<template>
    <el-menu 
      default-active=2
      router
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      >
      <el-menu-item index="1">
        <i class="el-icon-edit"></i>
        <span slot="title">写报告</span>
      </el-menu-item>
      <el-menu-item index="2">
        <i class="el-icon-view"></i>
        <span slot="title">报告列表</span>
      </el-menu-item>
      <el-menu-item index="3">
        <i class="el-icon-info"></i>
        <span slot="title">bug列表</span>
      </el-menu-item>
    </el-menu>
</template>

<script>
  export default {
    methods: {
    
    }
  }
</script>

<style>

</style>