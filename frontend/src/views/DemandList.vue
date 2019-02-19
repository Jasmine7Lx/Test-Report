 <template>
 <div>
    <el-button type="text" @click="dialogVisible = true">添加需求</el-button>
    <el-dialog title="表单弹框" :visible.sync="dialogVisible" width="30%">
     <el-form  ref="demandForm" :rules="rules" :model="demandForm" label-width="110px" size="small">
        <el-form-item label="需求名称：" prop="name">
            <el-input v-model="demandForm.name" size="small" clearable placeholder="请填写"></el-input>
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
        <el-form-item label="产品负责人：" label-width="125px" prop="product">
            <el-select v-model="demandForm.product" size="small" filterable  placeholder="请选择" clearable>
                <el-option
                    v-for="item in productList"
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
    :data="demandList"
    style="width: 100%"
    height="440"
    highlight-current-row
    >
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="需求名称">
            <span>{{ props.row.name }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column
      label="创建时间"
      prop="create_time">
    </el-table-column>
    <el-table-column
      label="需求名称"
      prop="name">
    </el-table-column>
    <el-table-column
      label="产品负责人"
      prop="developer_name">
    </el-table-column>
    <el-table-column
      label="状态"
      prop="status">
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
export default {
    data() {
      return {
        testerList: [],
        productList: [],
        developerList: [],
        demandList: [],
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
    methods: {
        getTesters: function() {
          https.fetchGet('/api/tester')
          .then((resp) => {
            console.log(resp)
            this.testerList = resp.data.data;
          })
        },
        getProcduct: function() {
            https.fetchGet('/api/product')
            .then((resp) => {
                console.log(resp)
                this.productList = resp.data.data
            })
        },
        getDeveloper: function() {
            https.fetchGet('/api/developer')
            .then((resp) => {
                console.log(resp)
                this.developerList = resp.data.data
            })
        },
        getDemandList: function() {
            https.fetchGet('/api/demand')
            .then((resp) => {
                console.log(resp.data)
                this.demandList = resp.data.data
            })
        },
        AddDemand: function() {
            this.dialogVisible = false;
            https.fetchPost('/api/demandlist', this.demandForm)
            .then((resp) => {
                console.log(this.demandForm)
                this.$nextTick(()=>{this.$refs['demandForm'].resetFields();})
                this.getDemandList();
            })

        },
        reset: function() {
          this.$nextTick(()=>{this.$refs['demandForm'].resetFields();})
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
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
</style>