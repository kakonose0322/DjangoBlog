new Vue({
    el:'#index',
    data:{
        topmenu:[],
        banner:[],
        userUI:false,
        username:'',
        password:''
    },
    mounted(){
        // console.log(this.topmenu)
        this.getData()
        console.log(this)
    },
    methods:{
        getData:function () {
            var self = this;
            reqwest({
                url: '/api/index',
                method: 'get',
                type: 'json',
                success:function (data) {
                    // console.log(data)
                    self.topmenu = data.topmenu
                    self.banner = data.banner
                    console.log(self.topmenu)
                }
            })
        },
        userLogin:function() {
            var self = this
            reqwest({
                url: '/api/index',
                method: 'post',
                data:{
                    username:self.username,
                    password:self.password
                },
                success:function () {
                    console.log('ok')
                },
                error:function (err) {
                    console.log(err)
                }
            })
        },
        showUserUI: function(){
            this.userUI = !this.userUI
        }
    }
})