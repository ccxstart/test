import 'element-ui/lib/theme-chalk/index.css'
import 'element-ui/lib/index.js'
import Vue from 'vue'
import {
  Button, Table, TableColumn, Form, FormItem, Input, Message, Dialog, Link,
  Container, Header, Main, Row, Col, Footer, Tabs, TabPane, Menu, MenuItem, Pagination,
  Select, Option, Icon, Avatar, Dropdown, DropdownMenu, DropdownItem, Loading
} from 'element-ui'

Vue.use(Button)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Dialog)

Vue.use(Loading)

Vue.use(Container)
Vue.use(Header)
Vue.use(Main)
Vue.use(Row)
Vue.use(Col)
Vue.use(Footer)

Vue.use(Tabs)
Vue.use(TabPane)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(Link)
Vue.use(Pagination)

Vue.use(Select)
Vue.use(Option)
Vue.use(Icon)
Vue.use(Avatar)
Vue.use(Dropdown)
Vue.use(DropdownItem)
Vue.use(DropdownMenu)

Vue.prototype.$msg = Message
