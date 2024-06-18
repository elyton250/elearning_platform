import { Button } from "@/components/ui/button";
// import { Link } from "lucide-react";
import Link  from "next/link";

const CoursesPage = () => {
    return ( 
        <div className="p-6"> 
            <Link href="/teacher/create">
                <Button>
                    New Coourse
                </Button>
            </Link>
        </div>
     );
}
 
export default CoursesPage;