<template>
  <div id="Login">
    <img class="bgc_img" src="../assets/back_pic.png" alt="">
    <div class="login_container">
      <div class="login_box">
        <div class="logo">
          <img src="../assets/logo.png" alt="">
        </div>
        <el-form ref="userRef" :rules="userRules" :model="userForm" label-width="0px" class="for_style">
          <el-form-item prop="name">
            <el-input v-model="userForm.name" type="primary" prefix-icon="el-icon-user-solid" placeholder="用户名"></el-input>
          </el-form-item>
          <el-form-item prop="pwd">
            <el-input v-model="userForm.pwd" show-password prefix-icon="el-icon-lock" placeholder="密码"></el-input>
          </el-form-item>
          <el-form-item class="btns">
            <el-button type="primary" @click="login">登录</el-button>
            <el-button @click="dialogVisible = true">注册</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
    <el-dialog title="注册用户" :visible.sync="dialogVisible" width="35%" :before-close="handleClose">
      <span slot="footer" class="dialog-footer">
        <el-form ref="registerForm" :rules="registerForm" :model="registerForm">
          <el-form-item label="用户名" prop="name">
            <el-input v-model="registerForm.name" prefix-icon="el-icon-user-solid" placeholder="用户名"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="pwd">
            <el-input v-model="registerForm.pwd" show-password prefix-icon="el-icon-lock" placeholder="密码"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="pwd">
            <el-input v-model="registerForm.real_pwd" show-password prefix-icon="el-icon-lock" placeholder="确认密码"></el-input>
          </el-form-item>
          <el-button @click="cancelUser">取 消</el-button>
          <el-button type="primary" @click="registerUser">确 定</el-button>
        </el-form>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      dialogVisible: false,
      userForm: {
        name: 'python',
        pwd: '123'
      },
      registerForm: {
        name: '',
        pwd: '',
        real_pwd: ''
      },
      userRules: {
        name: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 2, max: 9, message: '长度在 2 到 6 个字符', trigger: 'blur' }
        ],
        pwd: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    restForm () {
      this.$refs.userRef.resetFields()
    },
    login () {
      this.$refs.userRef.validate(async valid => {
        // console.log(this.$refs)
        // console.log(valid)
        if (!valid) return
        const { data: res } = await this.$axios.post('/user/login', this.$qs.stringify(this.userForm))
        // console.log(res)
        if (res.status === 200) {
          // 登录成功后，获取token，保存token，保存到sessionStorage中
          window.sessionStorage.setItem('token', res.data.token)
          // 登录成功之后
          this.$msg.success(res.msg)
          // 跳转成功页面
          await this.$router.push('/home')
        } else {
          // alert(res.msg)
          this.$msg.error(res.msg)
        }
      })
    },
    async registerUser () {
      // const name = this.registerForm.name
      // const pwd = this.registerForm.pwd
      const { data: res } = await this.$axios.post('/user/user', this.$qs.stringify(this.registerForm))
      // console.log(res)
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.$msg.success(res.msg)
      // 登录成功后，获取token，保存token，保存到sessionStorage中
      window.sessionStorage.setItem('token', res.data.token)
      this.$msg.success(res.msg)
      await this.$router.push('/home')
    },
    handleClose () {
      this.$refs.registerForm.resetFields()
      this.dialogVisible = false
    },
    cancelUser () {
      this.$refs.registerForm.resetFields()
      this.dialogVisible = false
    }
  }
}
</script>

<style scoped lang="less">
.login_container {
  background-color: #F5DEB3;
  height: 100%;
}
.login_box {
  width: 450px;
  height: 350px;
  border-radius: 45px;
  background-color: #00FFFF;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.logo {
  height: 80px;
  width: 80px;
  border: 1px solid #eee;
  padding: 10px;
  border-radius: 10%;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 0 #ddd;

  img {
    width: 100%;
    height: 100%;
  }
}

.for_style {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 10%;
  box-sizing: border-box;
}

.btns {
  display: flex;
  justify-content: flex-end;
}
.bgc_img {
  width: 100%;
  height: 1000%;
}
</style>
