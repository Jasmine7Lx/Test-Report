 <template>
 <div>
    <el-button type="text" @click="dialogVisible = true">添加需求</el-button>
    <el-dialog title="新增需求" :visible.sync="dialogVisible" width="30%">
     <el-form  ref="demandForm" :rules="rules" :model="demandForm" label-width="110px" size="small">
        <el-form-item label="需求名称：" prop="name">
            <el-input v-model="demandForm.name" size="small" clearable placeholder="请填写"></el-input>
        </el-form-item>  
        <el-form-item label="产品负责人：" :rule="rules" label-width="125px" prop="product">
            <el-select v-model="demandForm.product" size="small" filterable  placeholder="请选择" clearable>
                <el-option
                    v-for="item in productList"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="测试人员：" prop="tester">
            <el-select v-model="demandForm.tester" size="small" multiple filterable placeholder="请选择">
                <el-option
                    v-for="item in testerList"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="开发人员：" prop="developer">
            <el-select v-model="demandForm.developer" size="small" multiple filterable placeholder="请选择">
                <el-option
                    v-for="item in developerList"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="任务状态：" prop="status">
            <el-select v-model="demandForm.status" size="small" placeholder="请选择" clearable>
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
        <el-button type="primary" @click="AddDemand()">确 定</el-button>
        <el-button @click="reset(demandForm)">重置</el-button>
      </span>
    </el-dialog>
  <el-table
    :data="demandList.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
    style="width: 100%"
    height="440"
    highlight-current-row
    @row-click="getDetail"
    >
    <el-table-column type="expand">
      <template>
        <!-- <span>{{demandDetail.demand}}</span> -->
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
          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
 </div>
</template>

<script>
import https from '../https.js'
import moment from 'moment'
export default {
    data() {
      return {
        testerList: [],
        productList: [],
        developerList: [],
        demandList: [],
        demandDetail: [],
        statusList: [
            {
                id: 'no_summit',
                name: '未提测'
            },{
                id: 'summit',
                name: '已提测'
            },{
                id: 'completed',
                name: '已完成'

        }],
        rules: {
          name: [
            { required: true, message: '请输入活动名称', trigger: 'blur' }
          ],
          product: [
            { required: true, message: '请选择产品负责人', trigger: 'change' }
          ],
          status: [
            { required: true, message: '请选择任务状态', trigger: 'change' }
          ],

        },
        search: '',
        dialogVisible:false,
        demandForm: {
            name: '',
            tester: [],
            developer: [],
            product: '',
            status: '',
        }
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
        getTesters: function() {
          https.fetchGet('/api/tester')
          .then((resp) => {
            // console.log(resp)
            this.testerList = resp.data.data;
          })
        },
        getProcduct: function() {
            https.fetchGet('/api/product')
            .then((resp) => {
                // console.log(resp)
                this.productList = resp.data.data
            })
        },
        getDeveloper: function() {
            https.fetchGet('/api/developer')
            .then((resp) => {
                // console.log(resp)
                this.developerList = resp.data.data
            })
        },
        getDemandList: function() {
            https.fetchGet('/api/demand')
            .then((resp) => {
              // console.log(resp.data.data)
              this.demandList = resp.data.data
            })
        },
        AddDemand: function() {
            this.dialogVisible = false;
            https.fetchPost('/api/demandlist', this.demandForm)
            .then((resp) => {
                // console.log(this.demandForm)
                this.$nextTick(()=>{this.$refs['demandForm'].resetFields();})
                this.getDemandList();
            })
        },
        reset: function() {
          this.$nextTick(()=>{this.$refs['demandForm'].resetFields();})
        },
        formatDate: function(row, column) {
          const date = row[column.property]
          if (date === undefined) {
            return ''
          }
          //这里的格式根据需求修改
          return moment(date).format('YYYY-MM-DD')
        },
        getDetail: function(row) {
          let demandId = row.id
          https.fetchGet('/api/demandlist', {id:demandId})
          .then((resp) => {
              // console.log(resp.data)
              this.demandDetail = resp.data.data
              console.log(this.demandDetail)
          })
        }
    },
    created() {
      this.getTesters();
      this.getProcduct();
      this.getDeveloper();
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