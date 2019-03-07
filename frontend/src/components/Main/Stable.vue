<template>
  <header class="header">
    <h1>测试报告管理系统</h1>
    <div class="menu">
        <span class="name">
          <i style="margin-right: 10px"></i>
          Jasmine
        </span>
        <el-button type="primary" size="mini" icon="el-icon-setting" @click="Logout()">退出</el-button>
    </div>
  </header>
</template>

<script>
export default {
  methods: {
    Logout() {
      var self = this
      this.$confirm('您确定要退出吗?', '退出管理平台', {
        confirmButtonText: '确定',
        cancelButtonText: '取消'
      }).then(() => {
        self.$router.push({ path: '/login' })
      })
    }
  }
}
</script>


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


