<template >
  <el-container style="height:100%" direction="vertical">
    <el-header class="header" >
      <!-- 导航栏-->
      <stable></stable>
    </el-header>

    <el-container style="height: 615px;">
      <el-aside width="200px">
        <!-- 菜单栏 -->
        <report-menu></report-menu>
      </el-aside>
      <el-container style="border: 10px solid #eee">
        <el-main>
          <transition name="fade" mode="out-in">
            <router-view></router-view>
          </transition>
        </el-main>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
import Stable from "@/components/Main/Stable";
import ReportMenu from "@/components/Main/ReportMenu";
export default {
  name: "App",
  components: {
    reportMenu: ReportMenu,
    stable: Stable
  }
};
</script>

<style scoped >
html {
  height: 100%;
}
body {
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.header {
  background-color: rgb(64, 158, 255);
}
.el-aside {
  color: #333;
  background-color: #fff;
}
.el-row,
.el-col {
  height: 60px;
}
/* #head-title {
    color: #fafafa;
    letter-spacing: 0;
    text-shadow: 0px 1px 0px #999, 0px 2px 0px #888, 0px 3px 0px #777, 0px 4px 0px #666, 0px 5px 0px #555, 0px 6px 0px #444, 0px 7px 0px #333, 0px 8px 7px #001135;
    -webkit-background-clip : text;
    text-align: left;
    font-size: 40px;
  }
  #head-name {
    font-size: 15px ;
    -webkit-background-clip : text;
    margin: 0 auto;
    text-align: right;
  } */
/* 路由切换动效 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
</style>
