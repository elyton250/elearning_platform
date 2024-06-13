"use client";

import { UserButton } from "@clerk/nextjs";
import { usePathname } from "next/navigation";
import { useRouter } from "next/router";
import { Button } from "./ui/button";
import { LogOut } from "lucide-react";
import Link from "next/link"; // Import Link from next/link

export const NavbarRoutes = () => {
    const pathname = usePathname();
    // const router = useRouter();

    const isTeacherPage = pathname?.startsWith("/teacher");
    const isPlayerPage = pathname?.includes("/player");

    return (
        <div className="flex gap-x-2 ml-auto">
            {isTeacherPage || isPlayerPage ? (
               <Button>
                <LogOut className="h-4 w-4 mr-2"/>
                Exit
               </Button> 
            ): (
                <Link href="/teacher/courses">
                    <Button size="sm" variant="ghost">
                        Teacher Mode
                    </Button>
                
                </Link>
            )}
            <UserButton
            afterSignOutUrl="/"
            />
        </div>
    );
};
