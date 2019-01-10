<template>
  <div class="edit">
    <el-form  ref="form1" :rules="rules" model="form1" label-width="110px" size="small">
        <el-form-item label="需求名称：" prop="demand_name">
            <el-input v-model="form1.demand" placeholder="请输入需求名称" clearable></el-input>
        </el-form-item>
        <el-form-item label="测试人员：" prop="tester_name">
            <el-select v-model="form1.tester" @change="onSelectTester" size="small" multiple filterable placeholder="请选择">
                <el-option
                    v-for="item in testerList"
                    :key="item.id"
                    :label="item.developer_name"
                    :value="item.id">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="开发人员：" prop="developer_name">
            <el-select v-model="form1.developer" size="small" multiple filterable placeholder="请选择">
                <el-option                     
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="产品负责人：" prop="demander_name" label-width="125px" >
            <el-select v-model="form1.demander" size="small" multiple filterable placeholder="请选择">
                <el-option                     
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </el-form-item>
        <hr />

        <el-form-item label="一、测试结论：" label-width="140px" hide-required-asterisk="true" prop="test_result">
            <el-radio-group v-model="test_result">
                <el-radio :label="1">测试通过</el-radio>
                <el-radio :label="2">测试不通过</el-radio>
                <el-radio :label="3">测试完成</el-radio>
            </el-radio-group>   
        </el-form-item>        
    </el-form>

    <div class="edit2">
        <el-form label-position="top" ref="form2" :rules="rules" :model="form2" size="small">
            <el-form-item>
                <span style="font-size:16.5px; padding-left:10px;">二、遗留问题：</span>
                <el-button type="primary" size="mini" @click.native="AddList(form2.is_remain)">添加</el-button>
                <el-row v-for="item of form2.is_remain" :key="item">
                    <el-col :span="10">
                        <el-input v-model="item.remain" size="small" clearable></el-input>
                    </el-col>
                    <el-button type="danger" icon="el-icon-delete" round @click.native.prevent="removeList(item,form2.is_remain)" title="删除"></el-button>
                    <el-dropdown trigger="click"  style="margin-left: 10px;color: #20a0ff;">
                        <el-button>移动<i class="el-icon-caret-bottom el-icon-right"></i>
                        </el-button>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item @click.native="moveTop(item,form2.is_remain)">置顶</el-dropdown-item>
                            <el-dropdown-item @click.native="moveUp(item,form2.is_remain)">上移</el-dropdown-item>
                            <el-dropdown-item @click.native="moveDown(item,form2.is_remain)">下移</el-dropdown-item>
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
                    <el-radio-group v-model="test_enviroment">
                        <el-radio :label="1">正式环境</el-radio>
                        <el-radio :label="2">测试环境</el-radio>
                        <el-radio :label="3">灰度环境</el-radio>
                    </el-radio-group>
                </el-row >
                <el-row>
                    <span class="explain">2.环境配置：</span>
                    <el-button type="primary" size="mini" @click.native="AddList(form2.is_configure)">添加</el-button>
                </el-row>
                <el-row v-for="item of form2.is_configure" :key="item" >
                    <el-col :span="10" >
                        <el-input v-model="item.configure" size="small" clearable></el-input>
                    </el-col>
                    <el-col :span="10">
                        <el-button type="danger" icon="el-icon-delete" round  @click.native.prevent="removeList(item,form2.is_configure)" title="删除"></el-button>
                    </el-col>
                </el-row>
                <el-row>
                    <span class="explain">3.测试版本/链接：</span>
                    <el-button type="primary" size="mini" @click.native="AddList(form2.is_build)">添加</el-button>
                </el-row>
                <el-row v-for="item of form2.is_build" :key="item">
                    <el-col :span="10">
                        <el-input v-model="item.build" size="small" clearable></el-input>
                    </el-col>
                    <el-col :span="10">
                        <el-button type="danger" icon="el-icon-delete" round  @click.native.prevent="removeList(item,form2.is_build)" title="删除"></el-button>
                    </el-col>
                </el-row>
                <el-row>
                    <span class="explain">4.测试时间：</span>
                    <el-date-picker
                        v-model="test_time"
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
                    <el-button type="primary" size="mini" @click.native="AddList(form2.is_frontbug)">添加</el-button>
                </el-row>
                <el-row v-for="item of form2.is_frontbug" :key="item" >
                     <el-col :span="10">
                        <el-input v-model="item.frontbug" size="small" clearable></el-input>
                    </el-col>
                    <el-col :span="10">
                        <el-radio-group v-model="item.solve">
                            <el-radio :label="item.id" :key="item.key" v-for="item in form2.solveproblem">{{item.name}}</el-radio>
                        </el-radio-group>
                    <el-button type="danger" icon="el-icon-delete" round  @click.native.prevent="removeList(item,form2.is_frontbug)" title="删除"></el-button>
                    </el-col>
                </el-row>
                <el-row>
                    <span class="explain">2.后端bug：</span>
                    <el-button type="primary" size="mini" @click.native="AddList(form2.is_backbug)">添加</el-button>
                </el-row>
                <el-row v-for="item of form2.is_backbug" :key="item" >
                     <el-col :span="10">
                        <el-input v-model="item.backbug" size="small" clearable></el-input>
                    </el-col>
                    <el-col :span="10">
                        <el-radio-group v-model="item.solve">
                            <el-radio :label="item.id" :key="item.key" v-for="item in form2.solveproblem">{{item.name}}</el-radio>
                        </el-radio-group>
                    <el-button type="danger" icon="el-icon-delete" round  @click.native.prevent="removeList(item,form2.is_backbug)" title="删除"></el-button>
                    </el-col>
                </el-row>
            </el-form-item>
        </el-form>

        <el-form class="edit3">
            <el-form-item>
                <span style="font-size:16.5px; padding-left:10px;">五、兼容性：</span>
                <el-row>
                    <el-col>
                    <span class="explain">1.电脑系统：</span>
                    <el-select
                        v-model="computer"
                        multiple
                        filterable
                        allow-create
                        default-first-option
                        placeholder="请选择已测试的系统">
                        <el-option
                            v-for="item in form3.computer_system"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col>
                    <span class="explain">2.浏览器：</span>
                    <el-select
                        v-model="browser"
                        multiple
                        filterable
                        allow-create
                        default-first-option
                        placeholder="请选择已测试的系统">
                        <el-option
                            v-for="item in form3.browser_system"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                    </el-col>
                </el-row>
            </el-form-item>
        </el-form>
        <el-form class="edit4" :model="form4">
            <span style="font-size:16.5px; padding-left:10px;">六、测试用例：</span>
            <el-form-item>
                <span class="explain">链接：</span>
                <el-input size="small" v-model="form4.caselink"></el-input>
            </el-form-item>
            <el-form-item>
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
                <el-button type="primary" @click="submitForm(edit_form)">立即创建</el-button>
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
        options: [{
          value: 1,
          label: '小A'
        }, {
          value: 2,
          label: '小B'
        },
        {
          value: 3,
          label: '小C'
        }],
        test_result: "",
        test_enviroment: "",
        test_time: '',
        computer: [],
        browser: [],
        edit_form: ['form1','form2','form3','form4'],
        rules: {
            demand_name:[
                {required:true, message:'请输入需求名称',trigger:'blur'}
            ],
            tester_name:[
                {required:true, message:'请输入测试人员',trigger:'blur'}
            ],
            developer_name:[
                {required:true, message:'请输入开发人员',trigger:'blur'}
            ],
            demander_name:[
                {required:true, message:'请输入产品负责人',trigger:'blur'}
            ],
            test_result:[
                {required:true, message:'请选择',trigger:'blur'}
            ]
        },
        form1: {
            demand_name: '',
            tester: [],
            developer: [],
            demander: [],
        },
        form2: {
            is_remain: [{
                remain: '',
            }],
            is_configure: [{
                configure: '',
            }],
            is_build: [{
                build: '',
            }],
            is_frontbug: [{
                solve: '',
                frontbug: '',
            }],
            is_backbug:[{
                solve: '',
                backbug: '',
            }],
            boxs: [],
            solveproblem: [
                {
                    id: "sovle",
                    name: "已解决",
                    selected: "1",
                },
                {
                    id: "no_solve",
                    name: "未解决",
                    selected: "0",
                },
                {
                    id: "noneed_solve",
                    name: "无需解决",
                    selected: "-1",                    
                }
            ],

        },
        form3: {
            computer_system: 
            [
                {
                    value: 'win7',
                    label: 'windows 7'
                },
                {
                    value: 'win8',
                    label: 'window 8'
                }
            ],
            browser_system: [
                {
                    value: 'google',
                    label: '谷歌浏览器'
                },
                {
                    value: 'firefox',
                    label: '火狐浏览器'
                },
                {
                    value: 'ie 8',
                    label: 'IE8 浏览器'
                }
            ]
        },
        form4: {
            caselink: '',
        },
        // 用来暂时存放异步数据
        testerList: [],
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
        onSelectTester : function(value){

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
        submitForm(forms) {
            console.log(forms)
        },
        resetForm: function(forms) {

        }
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