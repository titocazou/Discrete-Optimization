using System;

namespace TravelingSalesman
{
    /// <summary>
    /// A simple city node class
    /// </summary>
    public class Node
    {
        readonly int index;

        /// <summary>
        /// Gets the index.
        /// </summary>
        /// <value>The index.</value>
        public int Index { get { return index; } }

        /// <summary>
        /// Gets the x.
        /// </summary>
        /// <value>The x.</value>
        public double X { get; private set; }

        /// <summary>
        /// Gets the y.
        /// </summary>
        /// <value>The y.</value>
        public double Y { get; private set; }

        /// <summary>
        /// Calculates the distance between two nodes
        /// </summary>
        /// <param name="n1">The first node</param>
        /// <param name="n2">The second node</param>
        /// <returns>the distance</returns>
        public static double DistanceBetween(Node n1, Node n2)
        {
            return ((n1.X - n2.X) * (n1.X - n2.X) + (n1.Y - n2.Y) * (n1.Y - n2.Y));
        }

        /// <summary>
        /// Calculates the distance to another node
        /// </summary>
        /// <param name="other">The other node</param>
        /// <returns>the distance</returns>
        public double DistanceTo(Node other)
        {
            return DistanceBetween(this, other);
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="Node"/> class.
        /// </summary>
        /// <param name="index">The index.</param>
        /// <param name="x">The x.</param>
        /// <param name="y">The y.</param>
        public Node(int index, double x, double y)
        {
            this.index = index;
            X = x;
            Y = y;
        }

        /// <summary>
        /// Serves as a hash function for a <see cref="Node"/> object.
        /// </summary>
        /// <returns>A hash code for this instance that is suitable for use in hashing algorithms and data structures such as a
        /// hash table.</returns>
        public override int GetHashCode()
        {
            return Index.GetHashCode();
        }

        /// <summary>
        /// Determines whether the specified <see cref="System.Object"/> is equal to the current <see cref="Node"/>.
        /// </summary>
        /// <param name="obj">The <see cref="System.Object"/> to compare with the current <see cref="Node"/>.</param>
        /// <returns><c>true</c> if the specified <see cref="System.Object"/> is equal to the current <see cref="Node"/>;
        /// otherwise, <c>false</c>.</returns>
        public override bool Equals(object obj)
        {
            var casted = obj as Node;
            if (casted == null)
                return false;
            return casted.Index == Index;
        }
    }
}

