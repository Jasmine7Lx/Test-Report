<template>
  <el-table
    :data="reportList.filter(data => !search || data.demand_name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%"
    height="440"
    highlight-current-row
    >
    <el-table-column
      label="创建时间"
      prop="create_time">
    </el-table-column>
    <el-table-column
      label="需求名称"
      prop="demand_name">
    </el-table-column>
    <el-table-column
      label="提交人"
      prop="developer_name">
    </el-table-column>
    <el-table-column
      align="right">
      <template slot="header" slot-scope="scope">
        <el-input
          v-model="search"
          size="mini"
          placeholder="输入关键字搜索"/>
      </template>
      <template slot-scope="scope">
        <el-button
          size="mini"
          type="danger"
          @click="handleDetail(scope.$index, scope.row)">查看</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import https from '../../https.js'
export default {
    data() {
      return {
        search: '',
        reportList: [],
      }
    },
    methods: {
      getReportList: function() {
        https.fetchGet('/api/reportlist')
        .then((resp) => {
          console.log(resp.data)
          this.reportList = resp.data.reportlist
        })
      },
      handleDetail(index, row) {
        console.log(index, row.id);
        this.$router.push({
          path:`/report/detail/${row.id}`
        })
      }
    },
    created() {
      this.getReportList();
    }
}
</script>

<style>
.el-table-column {
  background-color: midnightblue
}
</style>