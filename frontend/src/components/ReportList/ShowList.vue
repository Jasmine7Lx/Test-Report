<template>
  <el-table
    :data="reportList.filter(data => !search || data.demand_name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%"
    height="440"
    highlight-current-row
    :default-sort = "{prop: 'create_time', order: 'descending'}"
    >
    <el-table-column
      label="创建时间"
      prop="create_time"
      sortable
      :formatter="formatDate">
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
import moment from 'moment'
export default {
    data() {
      return {
        search: '',
        reportList: [],
      }
    },
    methods: {
      getReportList: function() {
        https.fetchGet('/api/reportlistall')
        .then((resp) => {
          console.log(resp.data)
          this.reportList = resp.data.reportlist
        })
      },
      handleDetail(index, row) {
        this.$router.push({
          path:`/report/detail/${row.id}`
        })
      },
      formatDate: function(row, column) {
        console.log(row, column)
        const date = row[column.property]
        if (date === undefined) {
          return ''
        }
        //这里的格式根据需求修改
        return moment(date).format('YYYY-MM-DD')
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