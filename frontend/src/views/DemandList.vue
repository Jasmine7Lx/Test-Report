<template>
 <div>
  <add></add>
    <el-dialog title="更新需求" :visible.sync="dialogVisible" width="30%">
     <el-form label-width="110px" size="small" ref="editForm" v-model="editForm">
        <el-form-item label="任务状态：" prop="status">
            <el-select v-model="status" size="small" clearable :disabled="disabledChange">
                <el-option
                    v-for="item in statusList"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
     </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="EditDemand()">确 定</el-button>
      </span>
    </el-dialog>

  <el-table
    :data="demandList.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%"
    height="440"
    highlight-current-row
    @row-click="getDemandDetail"
    >
    <el-table-column type="expand">
      <template>
         <el-form label-position="left" class="table-expand" >
          <el-form-item label="需求名称：">
            <span>{{ Demands }}</span>
          </el-form-item>  
          <el-form-item label="产品负责人：">
            <span>{{ Products }}</span>
          </el-form-item> 
          <el-form-item label="前端开发：">
            <span v-for="web in Webs" :key="web.index" style="padding-right:15px">{{ web }}</span>
          </el-form-item>  
          <el-form-item label="后台开发：">
            <span v-for="background in Backgrounds" :key="background.index" style="padding-right:15px">{{ background }}</span>
          </el-form-item>  
          <el-form-item label="移动端开发：">
            <span v-for="app in Apps" :key="app.index" style="padding-right:15px">{{ app }}</span>
          </el-form-item>  
          <el-form-item label="测试人员：">
            <span v-for="tester in Testers" :key="tester.index" style="padding-right:5px">{{ tester }}  </span>
          </el-form-item>   
          </el-form>
       </template>
    </el-table-column>

    <el-table-column
      label="创建时间"
      prop="create_time"
      :formatter="formatDate">
    </el-table-column>
    <el-table-column
      label="需求名称"
      prop="name">
    </el-table-column>
    <el-table-column
      label="状态"
      prop="status">
    </el-table-column>
    <el-table-column
      align="right">
      <template slot="header">
        <el-input
          v-model="search"
          size="mini"
          placeholder="输入关键字搜索"/>
      </template>
      <template slot-scope="scope">
        <el-button
          size="mini"
          icon="el-icon-refresh"
          @click="getDetail(scope.$index, scope.row)">更新状态
        </el-button>
        <el-button
          size="mini"
          type="danger"
          @click="DeleteDemand(scope.$index, scope.row)">删除
        </el-button>
      </template>
    </el-table-column>
  </el-table>
 </div>
</template>

<script>
import https from '../https.js'
import moment from 'moment'
import Add from "@/components/Demand/Add";
export default {
    components: {
      add: Add
    },
    data() {
      return {
        testerList: [],
        productList: [],
        developerList: [],
        demandList: [],
        demandDetail: [],
        demandId: 0,
        editForm: [],
        statusList: [
            {
                id: "no_summit",
                name: "未提测"
            },{
                id: "summit",
                name: "已提测"
            },{
                id: "completed",
                name: "已完成"
        }],
        search: '',
        dialogVisible: false,
        disabledChange: false,
        status: ''
      }
    },
    computed: {
      Demands: function(){
        if(this.demandDetail.demand){
          return this.demandDetail.demand[0].name
        }
      },
      Products: function(){
        if(this.demandDetail.product){
          return this.demandDetail.product[0].name
        }
      },
      Webs: function(){
        if(this.demandDetail.web){
          var web = []
          for(let i in this.demandDetail.web){
            var webs = this.demandDetail.web[i]
            for(let a in webs){
              web[i] = webs[a]
            }
          }
          return web
        }
      },
      Backgrounds: function(){
        if(this.demandDetail.background){
          var back = []
          for(let i in this.demandDetail.background){
            var backgrounds = this.demandDetail.background[i]
            for(let a in backgrounds){
              back[i] = backgrounds[a]
            }
          }
          return back
        }
      },
      Apps: function(){
        if(this.demandDetail.app){
          var app = []
          for(let i in this.demandDetail.app){
            var apps = this.demandDetail.app[i]
            for(let a in apps){
              app[i] = apps[a]
            }
          }
          return app
        }
      },
      Testers: function(){
        if(this.demandDetail.tester){
          var tes = []
          for(let i in this.demandDetail.tester){
            var testers = this.demandDetail.tester[i]
            for(let a in testers){
              tes[i] = testers[a]
            }
          }
          return tes
        }
      },
    },
    methods: {
        getDemandList: function() {
            https.fetchGet('/api/demand')
            .then((resp) => {
              this.demandList = resp.data.data
            })
        },
        getDetail: function(index,row) {
          this.dialogVisible = true
          this.demandId = row.id
          this.status = row.status
          if(this.status == "已完成"){
            this.disabledChange = true
          }
        },
        EditDemand:function(index,row) {
          console.log(this.demandId,this.status)
          https.fetchGet('/api/editdemand', {id:this.demandId, status:this.status})
          .then((resp) => {
            this.dialogVisible = false;
            // this.$nextTick(()=>{this.$refs['editForm'].resetFields();})
            this.getDemandList();
          })
          // this.$router.push({
          //   path:`/demand/list`
          // })
        },
        formatDate: function(row, column) {
          const date = row[column.property]
          if (date === undefined) {
            return ''
          }
          //这里的格式根据需求修改
          return moment(date).format('YYYY-MM-DD')
        },
        getDemandDetail: function(row) {
          let demandId = row.id
          https.fetchGet('/api/demandlist', {id:demandId})
          .then((resp) => {
              this.demandDetail = resp.data.data
          })
        }
    },
    created() {
      this.getDemandList();
    }
}
</script>

<style>
.el-table-column {
  background-color: midnightblue
}
.table-expand label {
  width: 100px;
  color: #99a9bf;
}
.table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
</style>