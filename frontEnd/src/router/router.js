import Project from "../components/Project.vue"
import ProjectDetail from "../components/ProjectDetail.vue"
import InterfaceDetail from "../components/InterfaceDetail.vue"
import VAView from "../components/VAView.vue"

const routers = [
  {path:'*', redirect:"/Project"},
  {path:'/Project', component:Project},
  {path:'/ProjectDetail/:projectName', component:ProjectDetail},
  {path:'/Project/:projectName/InterfaceDetail/:interId', component:InterfaceDetail},
  {path:'/VAView/:VAName', component:VAView},
]

export default routers
