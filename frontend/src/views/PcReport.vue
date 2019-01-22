<template>
  <div class="edit">
    <el-form  ref="form1"  model="form1" label-width="110px" size="small">
        <el-form-item label="需求名称：">
            <el-select v-model="form1.demand" @change="onSelectDemand" size="small"  placeholder="请选择">
                <el-option
                    v-for="item in demandList"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>  
        <el-form-item label="测试人员：">
            <el-select v-model="form1.tester" size="small" multiple filterable placeholder="请选择">
                <el-option
                    v-for="item in testerList"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="开发人员：">
            <el-select v-model="form1.developer" size="small" multiple filterable placeholder="请选择">
                <el-option
                    v-for="item in developerList"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="产品负责人：" label-width="125px" >
            <el-select v-model="form1.product" size="small" multiple filterable placeholder="请选择">
                <el-option
                    v-for="item in productList"
                    :key="item.id"
                    :label="item.name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <hr />

        <el-form-item label="一、测试结论：" label-width="140px" hide-required-asterisk="true">
            <el-radio-group v-model="form1.result">
                <el-radio v-for="item of results" :key="item.index" :label="item.id">{{item.name}}</el-radio>
            </el-radio-group>
        </el-form-item>
    </el-form>

    <div class="edit2">
        <el-form label-position="top" ref="form2" :model="form2" size="small">
            <el-form-item>
                <span style="font-size:16.5px; padding-left:10px;">二、遗留问题：</span>
                <el-button type="primary" size="mini" @click.native="AddList(form2.remains)">添加</el-button>
                <el-row v-for="item of form2.remains" :key="item.key">
                    <el-col :span="10">
                        <el-input v-model="item.remain" size="small" clearable></el-input>
                    </el-col>
                    <el-button type="danger" icon="el-icon-delete" round @click.native.prevent="removeList(item,form2.remains)" title="删除"></el-button>
                    <el-dropdown trigger="click"  style="margin-left: 10px;color: #20a0ff;">
                        <el-button>移动<i class="el-icon-caret-bottom el-icon-right"></i>
                        </el-button>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item @click.native="moveTop(item,form2.remains)">置顶</el-dropdown-item>
                            <el-dropdown-item @click.native="moveUp(item,form2.remains)">上移</el-dropdown-item>
                            <el-dropdown-item @click.native="moveDown(item,form2.remains)">下移</el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown>
                </el-row>
                <!-- <el-row>
                    <el-col :span="14" :offset="5">
                        <el-button :span="24" type="primary" size="small" @click.native="AddList(form2.is_remain)">添加</el-button>
                    </el-col>
                </el-row> -->
            </el-form-item>
            <el-form-item>
                <span style="font-size:16.5px; padding-left:10px;">三、测试说明：</span>
                <el-row>
                    <span class="explain">1.测试环境：</span>
                    <el-radio-group v-model="form2.environment">
                        <el-radio v-for="item of enviroments" :key="item.index" :label="item.id">{{item.name}}</el-radio>
                    </el-radio-group>
                </el-row >
                <el-row>
                    <span class="explain">2.环境配置：</span>
                    <el-button type="primary" size="mini" @click.native="AddList(form2.configs)">添加</el-button>
                </el-row>
                <el-row v-for="item of form2.configs" :key="item.key" >
                    <el-col :span="10" >
                        <el-input v-model="item.config" size="small" clearable></el-input>
                    </el-col>
                    <el-col :span="10">
                        <el-button type="danger" icon="el-icon-delete" round  @click.native.prevent="removeList(item,form2.configs)" title="删除"></el-button>
                    </el-col>
                </el-row>
                <el-row>
                    <span class="explain">3.测试版本/链接：</span>
                    <el-button type="primary" size="mini" @click.native="AddList(form2.builds)">添加</el-button>
                </el-row>
                <el-row v-for="item of form2.builds" :key="item.key">
                    <el-col :span="10">
                        <el-input v-model="item.build" size="small" clearable></el-input>
                    </el-col>
                    <el-col :span="10">
                        <el-button type="danger" icon="el-icon-delete" round  @click.native.prevent="removeList(item,form2.builds)" title="删除"></el-button>
                    </el-col>
                </el-row>
                <el-row>
                    <span class="explain">4.测试时间：</span>
                    <el-date-picker
                        v-model="form2.time"
                        type="datetimerange"
                        range-separator="-"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期">
                        </el-date-picker>
                </el-row>
            </el-form-item>
            <el-form-item prop="solveproblem">
                <span style="font-size:16.5px; padding-left:10px;">四、测试中发现的问题：</span>
                <el-row>
                    <span class="explain">1.前端bug：</span>
                    <el-button type="primary" size="mini" @click.native="AddList(form2.frontbugs)">添加</el-button>
                </el-row>
                <el-row v-for="item of form2.frontbugs" :key="item.key" >
                     <el-col :span="10">
                        <el-input v-model="item.frontbug" size="small" clearable></el-input>
                    </el-col>
                    <el-col :span="10">
                        <el-radio-group v-model="item.solve">
                            <el-radio v-for="item in solveproblem" :key="item.index" :label="item.id">{{item.name}}</el-radio>
                        </el-radio-group>
                    <el-button type="danger" icon="el-icon-delete" round  @click.native.prevent="removeList(item,form2.frontbugs)" title="删除"></el-button>
                    </el-col>
                </el-row>
                <el-row>
                    <span class="explain">2.后端bug：</span>
                    <el-button type="primary" size="mini" @click.native="AddList(form2.backbugs)">添加</el-button>
                </el-row>
                <el-row v-for="item of form2.backbugs" :key="item.key" >
                     <el-col :span="10">
                        <el-input v-model="item.backbug" size="small" clearable></el-input>
                    </el-col>
                    <el-col :span="10">
                        <el-radio-group v-model="item.solve">
                            <el-radio v-for="item in solveproblem" :key="item.index" :label="item.id">{{item.name}}</el-radio>
                        </el-radio-group>
                    <el-button type="danger" icon="el-icon-delete" round  @click.native.prevent="removeList(item,form2.backbugs)" title="删除"></el-button>
                    </el-col>
                </el-row>
            </el-form-item>
        </el-form>

        <el-form class="edit3" :model="form3">
            <el-form-item>
                <span style="font-size:16.5px; padding-left:10px;">五、兼容性：</span>
                <el-row>
                    <el-col>
                    <span class="explain">1.电脑系统：</span>
                    <el-select
                        v-model="form3.computer"
                        multiple
                        filterable
                        default-first-option
                        placeholder="请选择已测试的系统">
                        <el-option
                            v-for="item in computerList"
                            :key="item.id"
                            :label="item.system"
                            :value="item.id">
                        </el-option>
                    </el-select>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col>
                    <span class="explain">2.浏览器：</span>
                    <el-select
                        v-model="form3.browser"
                        multiple
                        filterable
                        default-first-option
                        placeholder="请选择已测试的系统">
                        <el-option
                            v-for="item in browserList"
                            :key="item.id"
                            :label="item.system"
                            :value="item.id">
                        </el-option>
                    </el-select>
                    </el-col>
                </el-row>
            </el-form-item>
        </el-form>
        <el-form class="edit4" :model="form4">
            <span style="font-size:16.5px; padding-left:10px;">六、测试用例：</span>
            <el-form-item label="请选择用例类型：" class="explain">
                <el-select v-model="form4.type" @change="onSelectCase" size="small"  placeholder="请选择" >
                    <el-option
                        v-for="item in types"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>  
            <el-form-item v-if="case_type=='link'">
                <span class="explain">链接：</span>
                <el-input size="small" v-model="form4.link" ></el-input>
            </el-form-item>
            <el-form-item v-if="case_type=='file'">
                <span class="explain">文件：</span>
                <el-upload
                    class="upload-demo"
                    drag
                    action="https://jsonplaceholder.typicode.com/posts/"
                    multiple>
                    <i class="el-icon-upload"></i>
                    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                </el-upload>
            </el-form-item>
        </el-form>
        <el-row>
            <el-col :span="6" :offset="2">
                <el-button type="primary" @click="submitForm()">立即创建</el-button>
                <el-button @click="resetForm('edit_form')">重置</el-button>
            </el-col>
        </el-row>
    </div>


</div>
</template>

<script>
import https from '../https.js'
export default {
    data() {
      return {
        // options: [{
        //   value: 1,
        //   label: '小A'
        // }, {
        //   value: 2,
        //   label: '小B'
        // },
        // {
        //   value: 3,
        //   label: '小C'
        // }],
        // 用来暂时存放异步数据
        case_type : "link",
        testerList: [],
        productList: [],
        developerList: [],
        demandList: [],
        computerList: [],
        browserList: [],
        results: [
            {
                id: "pass",
                name: "测试通过"
            },
            {
                id: "block",
                name: "测试不通过"
            },
            {
                id: "finish",
                name: "测试完成"
            }
        ],
        enviroments: [
            {
                id: "formal",
                name: "正式环境"
            },
            {
                id: "test",
                name: "测试环境"
            },
            {
                id: "gray",
                name: "灰度环境"
        }],
        solveproblem: [
            {
                id: "sovle",
                name: "已解决",
            },
            {
                id: "no_solve",
                name: "未解决",
            },
            {
                id: "noneed_solve",
                name: "无需解决",
            }
        ],

        // rules: {
        //     demand:[
        //         {required:true, message:'请输入需求名称',trigger:'blur'}
        //     ],
        //     tester:[
        //         {required:true, message:'请输入测试人员',trigger:'blur'}
        //     ],
        //     developer:[
        //         {required:true, message:'请输入开发人员',trigger:'blur'}
        //     ],
        //     demander:[
        //         {required:true, message:'请输入产品负责人',trigger:'blur'}
        //     ],
        //     test_result:[
        //         {required:true, message:'请选择',trigger:'blur'}
        //     ]
        // },
        form1: {
            demand: '',
            tester: [],
            developer: [],
            product: [],
            result: "",
        },
        form2: {
            environment: "",
            time: '',
            remains: [{
                remain: '',
            }],
            configs: [{
                config: '',
            }],
            builds: [{
                build: '',
            }],
            frontbugs: [{
                solve: '',
                frontbug: '',
            }],
            backbugs:[{
                solve: '',
                backbug: '',
            }],
        },
        form3: {
            computer: [],
            browser: [],
        },
        types: [{
            value: "link",
            label: "链接",
        },
        {
            value: "file",
            label: "文件",
        }],
        form4: {
            type: '',
            link: '',
            file: []
        },
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
                console.log(resp)
                this.demandList = resp.data.data
            })
        },
        getComputerList: function() {
            https.fetchGet('/api/computer')
            .then((resp) => {
                console.log(resp)
                this.computerList = resp.data.data
            })
        },
        getBrowserList: function() {
            https.fetchGet('/api/browser')
            .then((resp) => {
                this.browserList = resp.data.data
            })
        },
        AddList: function(boxs) {
            var n = boxs ? boxs.length + 1 : 1;
            boxs.push({
                value: '',
                key: Date.now()
            });
        },
        removeList: function(item,boxs) {
            var index = boxs.indexOf(item);
            boxs.splice(index,1);
        },
        moveTop: function(item,boxs) {
            var index = boxs.indexOf(item);
            if (index != 0) {
                boxs.splice(index,1);
                boxs.splice(0,0,item);
            }
        },
        moveUp: function(item,boxs) {
            var index = boxs.indexOf(item);
            if(index != 0){
                boxs.splice(index,1);
                boxs.splice(index-1,0,item);
            }
        },
        moveDown: function(item,boxs) {
            var index = boxs.indexOf(item);
            var max = boxs.length;
            if(index != max){
                boxs.splice(index,1);
                boxs.splice(index+1,0,item);
            }
        },
        onSelectCase(val){
            if (val=="link"){
                this.case_type = "link"
            } else{
                this.case_type = "file"
            }
        },
        onSelectDemand(val){
            pass
        },
        // submitForm(forms) {
        //     console.log('summit')
        // },
        resetForm: function(forms) {
            console.log('reset')
        },
        submitForm: function() {
        //   var dataList={demand_id:'1'}
          https.fetchPost('/api/report', this.form3)
            .then((resp) => {
                console.log(this.form3)
            })
        },
    },
    created() {
      this.getTesters();
      this.getProcduct();
      this.getDeveloper();
      this.getDemandList();
      this.getComputerList();
      this.getBrowserList();
    }
}
</script>

<style>
body {
    min-width: 1200px;
    margin: 0 auto;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    color: #606266;
}
.edit .el-input {
    padding-top: 2px;
    width: 350px;
}
.edit2 .el-input {
    padding-left: 45px;
    width: 400px;
}
.edit3 .el-input {
    padding-left: 1px;
    width: 400px;
}
.edit4 .el-input {
    padding-left: 1px;
    width: 400px;
}
.el-upload {
    padding-left: 45px;
}
.el-form-item__label {
    font-size: 16.5px;
}

.explain {
    font-size: 15px;
    padding-left: 35px;
}
hr {
    width:100%;
    margin:0 auto;
    border: 0;
    height: 1px;
    background: rgb(195, 198, 223);
    background-image: linear-gradient(to right, #ccc, #99b0da, #ccc);
}
</style>
