<template>
  <el-container>
    <el-header>
    <el-row>
      <el-col :span="7">
        <div id="head-title">
          测试报告管理系统
        </div>
      </el-col>
      <el-col :span="17" id="head-name">
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
    </el-header>
    
  <el-container style="height: 615px; border: 1px solid #eee">
  <el-aside width="200px">
    <report-menu></report-menu>
  </el-aside>

    <el-main>
      <el-table :data="tableData">
        <el-table-column prop="date" label="日期" width="140">
        </el-table-column>
        <el-table-column prop="name" label="测试人员" width="140">
        </el-table-column>
        <el-table-column prop="address" label="需求名称">
        </el-table-column>
      </el-table>
    </el-main>
  </el-container>
</el-container>
</template>

<script>
import ReportMenu from './components/ReportMenu'
export default {
  name: 'App',
  components: {
     'report-menu': ReportMenu,
  }
}
</script>

<style>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;

  }
  
  .el-aside {
    color: #333;
    background-color: #545c64
  }

  .el-row,.el-col {
    height: 60px;
  }
  #head-title {
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
  }
</style>

<script>
  export default {
    data() {
      const item = {
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      };
      return {
        tableData: Array(10).fill(item)
      }
    }
  };
</script>