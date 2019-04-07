<template>
<div>
    <div class="d1">
        <el-select v-model="select_show" @change="onSeleteShow">
          <el-option
            v-for="item in showlist"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
    </div>
    <div style="padding-top: 45px">
      <hr />
    </div>
    <div>
      <el-table
        :data="reportList.filter(data => !search || data.demand_name.toLowerCase().includes(search.toLowerCase()))"
        style="width: 100%;font-size:16px"
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
   </div>
</div>
</template>

<script>
import https from '../https.js'
import moment from 'moment'
export default {
    data() {
      return {
        search: '',
        reportList: [],
        changeList: [],
        select_show: 'all',
        showlist: [{
            value: 'all',
            label: '查看全部'
          }, {
            value: 'pclist',
            label: '查看pc端报告'
          }, {
            value: 'applist',
            label: '查看移动端报告'
          }
        ]
      }
    },
    methods: {
      getReportList: function() {
        https.fetchGet('/api/reportlistall')
        .then((resp) => {
          // console.log(resp.data)
          this.reportList = resp.data.reportlist
        })
      },
      handleDetail(index, row) {
        if(row.report_type=='pc'){
          this.$router.push({
            path:`/report/detail/pc/${row.id}`
            
          })
        }
        else if(row.report_type=='app'){
          this.$router.push({
            path:`/report/detail/app/${row.id}`
            
          })
        } 
      },
      formatDate: function(row, column) {
        // console.log(row, column)
        const date = row[column.property]
        if (date === undefined) {
          return ''
        }
        //这里的格式根据需求修改
        return moment(date).format('YYYY-MM-DD')
      },
      onSeleteShow: function(item){
            if(item=="all"){
              https.fetchGet('/api/reportlistall')
              .then((resp) => {
                console.log(resp.data)
                this.reportList = resp.data.reportlist
              })
            }
            else if(item=="pclist"){
              https.fetchGet('/api/reportlistpc')
              .then((resp) => {
                // console.log(resp.data)
                this.reportList = resp.data.reportlist
              })
            }
            else if(item=="applist"){
              https.fetchGet('/api/reportlistapp')
              .then((resp) => {
                // console.log(resp.data)
                this.reportList = resp.data.reportlist
              })
            }
          }
    },
    created() {
      this.getReportList();
    }
}
</script>

<style>
.d1{
  float: left;
  padding-left: 5px;
}

.check {
    display: inline-block;
    padding-left: 15px;
    padding-top: 5px;
}
.el-table-column {
  background-color: midnightblue
}
/* .el-buttion {
  font-size:20px
} */
</style>
