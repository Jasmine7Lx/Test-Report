<template>
  <div class="edit">
    <el-form :rules="Form1Rule.rules" ref="form1" :model="form1" label-width="125px" size="small">
      <el-form-item prop="demand_name" label="需求名称:">
        <el-select v-model="form1.demand" @change="onSelectDemand" size="small" placeholder="请选择">
          <el-option v-for="item in demandList" :key="item.id" :label="item.name" :value="item.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item prop="tester_name" label="测试人员:">
        <el-select v-model="form1.tester" size="small" multiple filterable placeholder="请选择">
          <el-option v-for="item in testerList" :key="item.id" :label="item.name" :value="item.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item prop="developer_name" label="开发人员:">
        <el-select v-model="form1.developer" size="small" multiple filterable placeholder="请选择">
          <el-option
            v-for="item in developerList"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item prop="demander_name" label="产品负责人:">
        <el-select v-model="form1.product" size="small" multiple filterable placeholder="请选择">
          <el-option v-for="item in productList" :key="item.id" :label="item.name" :value="item.id"></el-option>
        </el-select>
      </el-form-item>
    </el-form>
    <hr>

    <div class="edit2">
      <el-form label-position="left" ref="form2" :model="form2" size="small" label-width="160px">
        <el-form-item label="一、测试结论:" hide-required-asterisk="true">
          <el-select v-model="form2.result" placeholder="请选择">
            <el-option
              v-for="item in TestResult"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="二、遗留问题:">
          <div v-for="(remain,index) in form2.remains" :key="index">
            <el-input v-model="remain.remain"></el-input>
            <el-button v-if="index!==0" :key="index" @click.prevent="removeList('remain',remain)">删除</el-button>
          </div>
          <el-button @click="addList('remain')">新增</el-button>
        </el-form-item>

        <el-form-item label="三、测试说明:">
          <br>
          <el-form label-position="left" label-width="125px" size="small">
            <el-form-item label="1.测试环境:">
              <el-select v-model="form2.environment" placeholder="请选择">
                <el-option
                  v-for="item in Environments"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                ></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="2.环境配置:">
              <div v-for="(config,index) in form2.configs" :key="index">
                <el-input v-model="config.config"></el-input>
                <el-button
                  type="danger"
                  icon="el-icon-delete"
                  round
                  @click.native.prevent="removeList('config',config)"
                  title="删除"
                  v-if="index!==0"
                ></el-button>
              </div>
              <el-button type="primary" @click="addList('config')">新增</el-button>
            </el-form-item>
            <el-form-item label="3.测试版本/链接:">
              <div v-for="(build,index) in form2.builds" :key="index">
                <el-input v-model="build.build"></el-input>
                <el-button
                  type="danger"
                  icon="el-icon-delete"
                  round
                  @click.native.prevent="removeList('build',build)"
                  title="删除"
                  v-if="index!==0"
                ></el-button>
              </div>
              <el-button type="primary" @click="addList('build')">新增</el-button>
            </el-form-item>
            <el-form-item label="4.测试时间:">
              <el-date-picker
                v-model="form2.time"
                @change="dataFormat"
                type="datetimerange"
                range-separator="-"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
              ></el-date-picker>
            </el-form-item>
          </el-form>
        </el-form-item>

        <el-form-item prop="solveproblem" label="四、测试中发现的问题:">
          <br>
          <el-form label-position="left" label-width="100px" size="small">
            <el-form-item label="1.前端bug:">
              <div v-for="(frontbug,index) in form2.frontbugs" :key="index">
                <el-input v-model="frontbug.frontbug"></el-input>
                <el-select v-model="frontbug.status" placeholder="请选择bug状态">
                  <el-option
                    v-for="item in BugsStatus"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  ></el-option>
                </el-select>
                <el-button
                  type="danger"
                  icon="el-icon-delete"
                  round
                  @click.native.prevent="removeBugs('front',frontbug)"
                  title="删除"
                  v-if="index!==0"
                ></el-button>
              </div>
              <el-button type="primary" @click="addBugs('front')">新增</el-button>
            </el-form-item>
            <el-form-item label="2.后端bug:">
              <div v-for="(backbug,index) in form2.backbugs" :key="index">
                <el-input v-model="backbug.backbug"></el-input>
                <el-select v-model="backbug.status" placeholder="请选择bug状态">
                  <el-option
                    v-for="item in BugsStatus"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  ></el-option>
                </el-select>
                <el-button
                  type="danger"
                  icon="el-icon-delete"
                  round
                  @click.native.prevent="removeBugs('back',backbug)"
                  title="删除"
                  v-if="index!==0"
                ></el-button>
              </div>
              <el-button type="primary" @click="addBugs('back')">新增</el-button>
            </el-form-item>
          </el-form>
        </el-form-item>

        <el-form-item label="五、兼容性:">
          <br>
          <el-form label-position="left" label-width="125px" size="small">
            <el-form-item label="1.电脑系统:">
              <el-select
                v-model="form3.computer"
                multiple
                filterable
                default-first-option
                placeholder="请选择已测试的系统"
              >
                <el-option
                  v-for="item in computerList"
                  :key="item.id"
                  :label="item.system"
                  :value="item.id"
                ></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="2.浏览器:">
              <el-select
                v-model="form3.browser"
                multiple
                filterable
                default-first-option
                placeholder="请选择已测试的系统"
              >
                <el-option
                  v-for="item in browserList"
                  :key="item.id"
                  :label="item.system"
                  :value="item.id"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-form>
        </el-form-item>

        <el-form-item label="六、测试用例:">
          <el-form label-position="left" label-width="125px" size="small">
            <el-form-item label="请选择用例类型:">
              <el-select
                v-model="form4.case_type"
                @change="onSelectCase"
                size="small"
                placeholder="请选择"
              >
                <el-option
                  v-for="item in types"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                ></el-option>
              </el-select>
            </el-form-item>
            <el-form-item v-if="case_type=='link'" label="链接:">
              <el-input size="small" v-model="form4.link"></el-input>
            </el-form-item>
            <el-form-item v-if="case_type=='file'" label="文件:">
              <el-upload
                class="upload-demo"
                drag
                action="https://jsonplaceholder.typicode.com/posts/"
                multiple
              >
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">
                  将文件拖到此处，或
                  <em>点击上传</em>
                </div>
              </el-upload>
            </el-form-item>
          </el-form>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="submitForm()">立即创建</el-button>
          <!-- <el-button @click="resetForm('edit_form')">重置</el-button> -->
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import https from "../https.js";
import { form1Rule } from "@/constants/rules";
import { testResult, environments, bugsStatus } from "@/constants/options";

export default {
  data() {
    return {
      // 用来暂时存放异步数据
      case_type: "link",
      testerList: [],
      productList: [],
      developerList: [],
      demandList: [],
      computerList: [],
      browserList: [],

      form1: {
        demand: "",
        tester: [],
        developer: [],
        product: []
      },
      form2: {
        result: "pass",
        environment: "test",
        time: "",
        remains: [
          {
            remain: ""
          }
        ],
        configs: [
          {
            config: ""
          }
        ],
        builds: [
          {
            build: ""
          }
        ],
        frontbugs: [
          {
            status: "",
            frontbug: ""
          }
        ],
        backbugs: [
          {
            status: "",
            backbug: ""
          }
        ]
      },
      form3: {
        computer: [],
        browser: []
      },
      types: [
        {
          value: "link",
          label: "链接"
        },
        {
          value: "file",
          label: "文件"
        }
      ],
      form4: {
        case_type: "",
        link: "",
        file: []
      }
    };
  },
  computed: {
    Form1Rule: () => form1Rule,
    TestResult: () => testResult,
    Environments: () => environments,
    BugsStatus: () => bugsStatus
  },

  methods: {
    dataFormat() {
      let time = this.form2.time;
      this.form2.time[0] = this.moment(time[0]).format("YYYY-MM-DD HH:mm:ss");
      this.form2.time[1] = this.moment(time[1]).format("YYYY-MM-DD HH:mm:ss");
    },
    addList(name) {
      this.form2[`${name}s`].push({
        [name]: ""
      });
    },
    removeList(name, item) {
      const index = this.form2[`${name}s`].indexOf(item);
      if (index !== -1) {
        this.form2[`${name}s`].splice(index, 1);
      }
    },
    addBugs(name) {
      this.form2[`${name}bugs`].push({
        status: "",
        [`${name}bug`]: ""
      });
    },
    removeBugs(name, item) {
      const index = this.form2[`${name}bugs`].indexOf(item);
      if (index !== -1) {
        this.form2[`${name}bugs`].splice(index, 1);
      }
    },
    getDemandList: function() {
      https.fetchGet("/api/demand").then(resp => {
        console.log(resp);
        this.demandList = resp.data.data;
      });
    },
    getComputerList: function() {
      https.fetchGet("/api/computer").then(resp => {
        console.log(resp);
        this.computerList = resp.data.data;
      });
    },
    getBrowserList: function() {
      https.fetchGet("/api/browser").then(resp => {
        this.browserList = resp.data.data;
      });
    },
    onSelectCase(val) {
      if (val == "link") {
        this.case_type = "link";
      } else {
        this.case_type = "file";
      }
    },
    onSelectDemand(item) {
      var demand_id = item;
      console.log(demand_id);
      https.fetchGet("/api/developerall", { id: demand_id }).then(resp => {
        console.log(resp.data);
      });
    },
    resetForm: function(forms) {
      console.log("reset");
    },
    submitForm: function() {
      var dataList = Object.assign(
        this.form1,
        this.form2,
        this.form3,
        this.form4
      );
      https.fetchPost("/api/pcreport", dataList).then(resp => {
        console.log(dataList);
        this.$router.push({ path: "/" });
      });
    }
  },
  created() {
    //   this.getTesters();
    //   this.getProcduct();
    //   this.getDeveloper();
    // this.getDemandList();
    // this.getComputerList();
    // this.getBrowserList();
  }
};
</script>

<style lang="css" scoped >

.el-input {
  width: auto;
}

hr {
  width: 100%;
  margin: 40px auto;
  border: 0;
  height: 1px;
  background: rgb(195, 198, 223);
  background-image: linear-gradient(to right, #ccc, #99b0da, #ccc);
}
</style>
