using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Event
    {
        public class Brigegroom
        {
            public delegate void MarryHandIer(string msg);
            public event MarryHandIer MarryEvent;

            public void OnMarruageComing(string msg)
            {
                if (MarryEvent != null)
                {
                    MarryEvent(msg);
                }
            }

        }
        public class friend
        {
            public string Name;
            public friend(string name)
            {
                this.Name = name;
            }
            public void SendMessage(string message)
            {
                Console.WriteLine(message);
                Console.WriteLine(this.Name + "收到了，到时候一定来哟！！");
            }
        }
        static void Main(string[] args)
        {
            Brigegroom brigegroom = new Brigegroom();
            friend friend1 = new friend("张三");
            friend friend2 = new friend("李四");
            friend friend3 = new friend("老赵");

            brigegroom.MarryEvent += new Brigegroom.MarryHandIer(friend1.SendMessage);
            brigegroom.MarryEvent += new Brigegroom.MarryHandIer(friend2.SendMessage);
            brigegroom.OnMarruageComing("朋友们，我的大喜之日马上到咯！！");
            Console.WriteLine("------------------------------------------------");
            Console.ReadLine();
        }
    }
}
