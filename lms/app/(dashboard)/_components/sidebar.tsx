import { Logo } from "./logo"
import { SidebarRoutes } from "./sidebar-routes";
export const Sidebar  = () => {
    return ( 
        <div className="h-full border-r flex felx-col overflow-y-auto bg-white shadow-sm">
            <div className="p-6">
                <Logo />
            </div>
            <div className="felx flex-col w-full">
                <SidebarRoutes />
            </div>
        </div>
     );
}
