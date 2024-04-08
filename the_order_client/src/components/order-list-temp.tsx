/**
 * This code was generated by v0 by Vercel.
 * @see https://v0.dev/t/vX9DuRrm6Ak
 */
import { CardTitle, CardHeader, CardContent, CardFooter, Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"

export function OrderListTemp() {
  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      <Card>
        <CardHeader className="flex flex-row items-center space-y-0">
          <CardTitle className="text-sm font-medium">Order #</CardTitle>
          <Button className="ml-auto h-6 w-6 rounded-full" size="icon" variant="outline">
            <CheckIcon className="h-3 w-3" />
            <span className="sr-only">Mark as complete</span>
          </Button>
        </CardHeader>
        <CardContent className="flex flex-col gap-2">
          <div className="text-sm font-medium">Sophia Anderson</div>
          <div className="text-sm text-gray-500 dark:text-gray-400">2 min ago</div>
        </CardContent>
        <CardFooter>
          <Button className="w-full" variant="outline">
            View order
          </Button>
        </CardFooter>
      </Card>
      <Card>
        <CardHeader className="flex flex-row items-center space-y-0">
          <CardTitle className="text-sm font-medium">Order #</CardTitle>
          <Button className="ml-auto h-6 w-6 rounded-full" size="icon" variant="outline">
            <CheckIcon className="h-3 w-3" />
            <span className="sr-only">Mark as complete</span>
          </Button>
        </CardHeader>
        <CardContent className="flex flex-col gap-2">
          <div className="text-sm font-medium">Ethan Williams</div>
          <div className="text-sm text-gray-500 dark:text-gray-400">5 min ago</div>
        </CardContent>
        <CardFooter>
          <Button className="w-full" variant="outline">
            View order
          </Button>
        </CardFooter>
      </Card>
      <Card>
        <CardHeader className="flex flex-row items-center space-y-0">
          <CardTitle className="text-sm font-medium">Order #</CardTitle>
          <Button className="ml-auto h-6 w-6 rounded-full" size="icon" variant="outline">
            <CheckIcon className="h-3 w-3" />
            <span className="sr-only">Mark as complete</span>
          </Button>
        </CardHeader>
        <CardContent className="flex flex-col gap-2">
          <div className="text-sm font-medium">Isabella Johnson</div>
          <div className="text-sm text-gray-500 dark:text-gray-400">10 min ago</div>
        </CardContent>
        <CardFooter>
          <Button className="w-full" variant="outline">
            View order
          </Button>
        </CardFooter>
      </Card>
    </div>
  )
}


function CheckIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <polyline points="20 6 9 17 4 12" />
    </svg>
  )
}
