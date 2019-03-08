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
  </div>
</template>
<script>
import https from '../../https.js'
export default {
    data() {
        return {
            testerList: [],
            productList: [],
            developerList: [],
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
            this.testerList = resp.data.data;
          })
        },
        getProcduct: function() {
            https.fetchGet('/api/product')
            .then((resp) => {
                this.productList = resp.data.data
            })
        },
        getDeveloper: function() {
            https.fetchGet('/api/developer')
            .then((resp) => {
                this.developerList = resp.data.data
            })
        },
        getDemandList: function() {
            https.fetchGet('/api/demand')
            .then((resp) => {
              this.demandList = resp.data.data
            })
        },
        AddDemand: function() {
            https.fetchPost('/api/demandlist', this.demandForm)
            .then((resp) => {
                this.getDemandList();
                this.dialogVisible = false;
                this.$nextTick(()=>{this.$refs['demandForm'].resetFields();})

            })
        },
        reset: function() {
          this.$nextTick(()=>{this.$refs['demandForm'].resetFields();})
        },
    },
    created() {
      this.getTesters();
      this.getProcduct();
      this.getDeveloper();
    //   this.getDemandList();
    }
}
</script>
<style>

</style>
