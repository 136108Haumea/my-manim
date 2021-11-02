#include <algorithm>
#include <vector>
#include <math.h>
#include <iostream>
using namespace std;
// ���±������鲻Ҫ�Ҹģ����ȴ󣬻���С�����п��ܳ�bug
// С��������
typedef vector<double> Point;

typedef vector<double> row_vector;

template<typename type>
auto operator / (const row_vector rv, const type n) {
	auto m = (double)n;
	row_vector v{};
	for (auto vi = rv.begin();vi != rv.end();++vi)
		v.push_back(*vi / m);
	return v;
}
template<typename type>
auto operator * (const type n, const row_vector rv) {
	auto m = (double)n;
	row_vector v{};
	for (auto vi = rv.begin();vi != rv.end();++vi)
		v.push_back(*vi * m);
	return v;
}
template<typename type>
auto operator * (const row_vector rv, const type n) {
	auto m = (double)n;
	row_vector v{};
	for (auto vi = rv.begin();vi != rv.end();++vi)
		v.push_back(*vi * m);
	return v;
}
auto operator + (const row_vector rv) {
	return rv;
}
auto operator + (const row_vector rv1, const row_vector rv2) {
	row_vector v{};
	for (auto vi = rv1.begin(), vj = rv2.begin();vi != rv1.end();++vi, ++vj)
		v.push_back(*vi + *vj);
	return v;
}
auto operator - (const row_vector rv) {
	return (-1) * rv;
}
auto operator - (const row_vector rv1, const row_vector rv2) {
	row_vector v{};
	for (auto vi = rv1.begin(), vj = rv2.begin();vi != rv1.end();++vi, ++vj)
		v.push_back(*vi - *vj);
	return v;
}

typedef vector<row_vector> Matrix;
template<typename type>
auto operator / (const Matrix mat, const type n) {
	auto m = (double)n;
	vector<row_vector> newmat{};
	for (auto mati = mat.begin();mati != mat.end();++mati)
		newmat.push_back(*mati / m);
	return newmat;
};

void print(Matrix mat) {
	printf("[");
	for (auto mati = mat.begin();mati != mat.end();++mati) {
		for (auto matj = (*mati).begin();matj != (*mati).end();++matj) {
			if (matj != (*mati).begin())
				printf(" ");
			cout << *matj;
		}
		if(mati+1 != mat.end())
			puts("");
	}
	printf("]");
}

Matrix operator + (Matrix mat1, Matrix mat2) {
	Matrix mat{};
	for (auto mati = mat1.begin(), matj = mat2.begin();mati != mat1.end();++mati, ++matj)
		mat.push_back(*mati + *matj);
	return Matrix(mat);

}

Matrix operator - (Matrix mat1, Matrix mat2) {
	Matrix mat{};
	for (auto mat1i = mat1.begin(), mat2i = mat2.begin();mat1i != mat1.end();++mat1i, ++mat2i) {
		row_vector mat_row{};
		for (auto mat1j = (*mat1i).begin(), mat2j = (*mat2i).begin();mat1j != (*mat1i).end();++mat1j, ++mat2j)
			mat_row.push_back(*mat1j - *mat2j);
		mat.push_back(mat_row);
	}
	return Matrix(mat);
}

Matrix operator * (Matrix mat1, Matrix mat2) {
	Matrix mat{};
	int m = mat1.size(), r = mat2[0].size(), n = mat2.size();
	for (int i = 0;i < m;i++) {
		row_vector mat_row{};
		for (int j = 0;j < r;j++) {
			double temp = 0;
			for (int k = 0;k < n;k++) 
				temp += (mat1[i][k] * mat2[k][j]);
			mat_row.push_back(temp);
		}
		mat.push_back(mat_row);
	}
	return Matrix(mat);
}

template<typename type>
auto operator * (const Matrix mat, const type n) {
	auto m = (double)n;
	vector<row_vector> newmat{};
	for (auto mati = mat.begin();mati != mat.end();++mati)
		newmat.push_back(*mati * m);
	return newmat;
};

template<typename type>
auto operator * (const type n, const Matrix mat) {
	auto m = (double)n;
	vector<row_vector> newmat{};
	for (auto mati = mat.begin();mati != mat.end();++mati)
		newmat.push_back(*mati * m);
	return newmat;
};


class numpy {
public:
    auto array(row_vector v) {
		return v;
	};
    auto lenght(row_vector rv) {
		double sqlenght = 0;
		for (auto vi = rv.begin();vi != rv.end();++vi)
			sqlenght += (*vi) * (*vi);
		return std::sqrt(sqlenght);
	};
	auto normalize(row_vector rv) {
		return rv / this->lenght(rv);
	};
	class linalg {
	public:
		auto determinant(Matrix mat) {
			auto limsize = min(mat.size(), mat[0].size());
			for (unsigned int i = 0;i + 1 < limsize;++i) {
				unsigned int swapj = i;
				while(swapj < limsize && mat[swapj][i] == 0)swapj++;
				if (swapj == limsize)return (double)0;
				if (i != swapj)mat[i] = -mat[i], swap(mat[i], mat[swapj]);
				for (unsigned int j = i + 1;j < limsize;++j)
					mat[j] = mat[j] - mat[j][i]/mat[i][i] * mat[i];
			}
			double det = 1;
			for (unsigned int i = 0;i < limsize;++i)
				det *= mat[i][i];
			return det;
		};
		auto det(Matrix mat) {
			/*write_string(mat);
			write_string(this->determinant(mat));*/
			return this->determinant(mat);
		};
	}linalg;
    auto cross(Point v1, Point v2) {
		return Point{
			v1[1] * v2[2] - v1[2] * v2[1],
			v1[2] * v2[0] - v1[0] * v2[2],
			v1[0] * v2[1] - v1[1] * v2[0] };
	};
    auto cross(Point p, Point q, Point b) {
		return this->linalg.det(Matrix({
			{p[0], p[1], 1},
			{q[0], q[1], 1},
			{b[0], b[1], 1} }));
	};
}np;

double PI = (double)acos(-1);
auto ev = pow(exp(1), PI) / pow(10, 6);//0.000023
auto ev_sq = ev * ev;

//���������
double Infinity = 333;

// �ж��������Ƿ���ȣ�С������ƽ��������ȣ�O(1)
auto point_is_equal(Point p, Point q) {
    // ��������ƽ��С������ƽ���������
    auto v = p - q;
    if (v[0]*v[0]+v[1]*v[1] < ev_sq)
        return true;
    return false;
};

// b������pq��Ϊ������Ϊ����O(1)
auto cross2(Point p, Point q, Point b) {
    return p[0]*q[1] - p[1]*q[0] + 
           q[0]*b[1] - q[1]*b[0] + 
           b[0]*p[1] - b[1]*p[0];
};

// ������b������pq��Ϊ������Ϊ����O(1)
auto ToLeft(Point p, Point q, Point b) {
    auto a = cross2(p, q, b);
    // С������Ϊ��������
    if (abs(a) < ev)
        return (double)0;
    // ����else abs(a) >= ev:
    return a;
};

// ��d��������pqb�ڣ�����True��O(1)
auto InTriangle(Point p, Point q, Point b, Point d) {
    auto tl1 = ToLeft(p, q, d);
    if (abs(tl1) < ev) {
        auto tl2 = ToLeft(q, b, d);
        auto tl3 = ToLeft(b, p, d);
        if (tl2 < ev && tl3 < ev || tl2 > -ev && tl3 > -ev)
            return true;
        return false;
    }
    if (tl1 > ev) {
        if (ToLeft(q, b, d) > -ev && ToLeft(b, p, d) > -ev)
            return true;
        return false;
    }
    if (tl1 < -ev) {
        if (ToLeft(q, b, d) < ev && ToLeft(b, p, d) < ev)
            return true;
        return false;
    }
    //�����ĸ���Ϊ0��������Ϊtl1==ev���ᷢ����
    return false;
};

// ��d������p, q, b�����Բ�⣬����True��O(1)
auto InCircle(Point p, Point q, Point b, Point d) {
    /*
    ��������Բ��ϵ
    \begin{ align }
    InCircle(p, q, b, d) = \begin{ vmatrix }
    x_p & y_p & x_p ^ 2 + y_p ^ 2 & 1\\
    x_q & y_q & x_q ^ 2 + y_q ^ 2 & 1\\
    x_b & y_b & x_b ^ 2 + y_b ^ 2 & 1\\
    x_d & y_d & x_d ^ 2 + y_d ^ 2 & 1\\
    \end{ vmatrix }\end{ align }
    */
    auto a13 = p[0] * p[0] + p[1] * p[1];
    auto a23 = q[0] * q[0] + q[1] * q[1];
    auto a33 = b[0] * b[0] + b[1] * b[1];
    auto a43 = d[0] * d[0] + d[1] * d[1];
    auto det = np.linalg.det({
        {p[0], p[1], a13, 1},
        {q[0], q[1], a23, 1},
        {b[0], b[1], a33, 1},
        {d[0], d[1], a43, 1},
        });
    if (det < -ev)
        return true;
    return false;
};

// �������ԲԲ�ģ�O(1)
auto CircumcircleCenter(Point p, Point q, Point b) {
    /*
    \begin{ align }
    &�������ԲԲ�Ĺ�ʽ\\
    & x = \frac{ 1 }{2}\begin{ vmatrix }
    1 & x_p ^ 2 + y_p ^ 2 & y_p\\
    1 & x_q ^ 2 + y_q ^ 2 & y_q\\
    1 & x_b ^ 2 + y_b ^ 2 & y_b\\
    \end{ vmatrix } / \begin{ vmatrix }
    1 & x_p & y_p\\
    1 & x_q & y_q\\
    1 & x_b & y_b\\
    \end{ vmatrix }\\
    & y = \frac{ 1 }{2}\begin{ vmatrix }
    1 & x_p & x_p ^ 2 + y_p ^ 2\\
    1 & x_q & x_q ^ 2 + y_q ^ 2\\
    1 & x_b & x_b ^ 2 + y_b ^ 2\\
    \end{ vmatrix } / \begin{ vmatrix }
    1 & x_p & y_p\\
    1 & x_q & y_q\\
    1 & x_b & y_b\\
    \end{ vmatrix }
    \end{ align }
    */
    auto a1 = p[0] * p[0] + p[1] * p[1];
    auto a2 = q[0] * q[0] + q[1] * q[1];
    auto a3 = b[0] * b[0] + b[1] * b[1];
    auto det1 = np.linalg.det({
        {1, p[0], p[1]},
        {1, q[0], q[1]},
        {1, b[0], b[1]},
        });
    if (det1 == 0) {
        printf("���㹲��");
        return p;
    }
    auto det2 = np.linalg.det({
        {1, a1, p[1]},
        {1, a2, q[1]},
        {1, a3, b[1]},
        });
    auto det3 = np.linalg.det({
        {1, p[0], a1},
        {1, q[0], a2},
        {1, b[0], a3},
        });
    return np.array({ det2 / det1, det3 / det1, 0 }) / 2;
};

/***������߽ṹ***/
// ��
class Face;
// ����
class Vertice;
// ���
class HalfEdge;
// Ͱ
class Bucket;

// ��
class Face {
public:
    // ��Ƿ�����
    bool visit = false;
    // ����������һ�����
    HalfEdge* halfedge;
    // ���Ӧ��Ͱ
    Bucket* bucket;
    // ���ԲԲ�ģ���άŵͼ��ʱ���õ�
    Point center;
    Face(HalfEdge *halfedge) {
        this->visit = false;
        this->halfedge = halfedge;
        this->bucket = nullptr;
        this->center = {Infinity, 0, 0};
    };
};

// ����
class Vertice {
public:
    // ��������
    Point point;
    // �ɶ���������һ�����
    HalfEdge* halfedge;
    Vertice(Point point) {
        this->point = point;
        this->halfedge = nullptr;
    };
};

// ���
class HalfEdge {
public:
    // ��Ƿ���
    bool visit = false;
    // �ߵ����
    Vertice* start;
    // �ߵ��յ�
    Vertice* end;
    // �ߵ������ֵ�
    HalfEdge* twin;
    // ������ڵ�ƽ��
    Face* face;
    // �ߵ�ǰ��
    HalfEdge* pre;
    // �ߵĺ��
    HalfEdge* suc;
    HalfEdge(Vertice *start, Vertice *end) {
        this->visit = false;
        this->start = start;
        this->end = end;
        this->twin = nullptr;
        this->face = nullptr;
        this->pre = nullptr;
        this->suc = nullptr;
    };
};

// Ͱ
class Bucket{
public:
    // ��Ƿ���
    bool visit = false;
    // Ͱװ�ĵ�
    vector<Point>points;
    // Ͱ��Ӧ����
    Face* face;
    Bucket(vector<Point>points) {
        this->visit = false;
        this->points = points;
        this->face = nullptr;
    };
};

// ��ʼ������������O(1)
auto InitInfNet(vector<Point>points) {
    // ��ʼ������Զ��
    // ��ʱ��
    /*auto pinfv1 = Vertice(np.array({ Infinity, 0, Infinity }));
    auto pinfv2 = Vertice(np.array({ 0, Infinity, Infinity }));
    auto pinfv3 = Vertice(np.array({ -Infinity, -Infinity, Infinity }));

    auto infv1 = &pinfv1;
    auto infv2 = &pinfv2;
    auto infv3 = &pinfv3;*/

    auto infv1 = new Vertice(np.array({ Infinity, 0, Infinity }));
    auto infv2 = new Vertice(np.array({ 0, Infinity, Infinity }));
    auto infv3 = new Vertice(np.array({ -Infinity, -Infinity, Infinity }));

    // ��ʼ������Զ���
    /*auto phalfedge1 = HalfEdge(infv1, infv2);
    auto phalfedge2 = HalfEdge(infv2, infv3);
    auto phalfedge3 = HalfEdge(infv3, infv1);
    auto phalfedgeTwin1 = HalfEdge(infv2, infv1);
    auto phalfedgeTwin2 = HalfEdge(infv3, infv2);
    auto phalfedgeTwin3 = HalfEdge(infv1, infv3);

    auto halfedge1 = &phalfedge1;
    auto halfedge2 = &phalfedge2;
    auto halfedge3 = &phalfedge3;
    auto halfedgeTwin1 = &phalfedgeTwin1;
    auto halfedgeTwin2 = &phalfedgeTwin2;
    auto halfedgeTwin3 = &phalfedgeTwin3;*/

    auto halfedge1 = new HalfEdge(infv1, infv2);
    auto halfedge2 = new HalfEdge(infv2, infv3);
    auto halfedge3 = new HalfEdge(infv3, infv1);
    auto halfedgeTwin1 = new HalfEdge(infv2, infv1);
    auto halfedgeTwin2 = new HalfEdge(infv3, infv2);
    auto halfedgeTwin3 = new HalfEdge(infv1, infv3);

    // ��ʼ���������ı�
    infv1->halfedge = halfedge1;
    infv2->halfedge = halfedge2;
    infv3->halfedge = halfedge3;

    // ��ʼ���������
    /*auto pface = Face(halfedge1);
    auto pfaceTwin = Face(halfedgeTwin1);

    auto face = &pface;
    auto faceTwin = &pfaceTwin;*/
    auto face = new Face(halfedge1);
    auto faceTwin = new Face(halfedgeTwin1);

    // ��ʼ�����������ߵ�ǰ������̣������ڵ���
    halfedge1->pre = halfedge3;
    halfedge1->suc = halfedge2;
    halfedge1->face = face;
    halfedge1->twin = halfedgeTwin1;

    halfedge2->pre = halfedge1;
    halfedge2->suc = halfedge3;
    halfedge2->face = face;
    halfedge2->twin = halfedgeTwin2;

    halfedge3->pre = halfedge2;
    halfedge3->suc = halfedge1;
    halfedge3->face = face;
    halfedge3->twin = halfedgeTwin3;

    // ��ʼ�����������ߵ�ǰ������̣������ڵ���
    halfedgeTwin1->pre = halfedgeTwin2;
    halfedgeTwin1->suc = halfedgeTwin3;
    halfedgeTwin1->face = faceTwin;
    halfedgeTwin1->twin = halfedge1;

    halfedgeTwin2->pre = halfedgeTwin3;
    halfedgeTwin2->suc = halfedgeTwin1;
    halfedgeTwin2->face = faceTwin;
    halfedgeTwin2->twin = halfedge2;

    halfedgeTwin3->pre = halfedgeTwin1;
    halfedgeTwin3->suc = halfedgeTwin2;
    halfedgeTwin3->face = faceTwin;
    halfedgeTwin3->twin = halfedge3;

    // ��ʼ��Ͱ����Ͱ���������еĵ�
    /*auto pbucket = Bucket(points);
    auto bucket = &pbucket;*/
    auto bucket = new Bucket(points);
    bucket->face = face;

    // ���Ӧ��Ͱ
    face->bucket = bucket;

    return face;
};
                                       
// �õ�����εĴ�������������ڲ��Խ��Ķ���Σ�����ʾ��ʱ�����Σ�����ʾ˳ʱ�����Σ����⿼��0��O(n)
auto get_polygon_directed_area(vector<Point> pol) {
    auto area = 0;
    auto size = pol.size();
    for (unsigned int i = 0;i < size;++i)
        area += pol[i][0] * pol[(i + 1) % size][1] - pol[(i + 1) % size][0];
    return area / 2;
};

// �߷�ת��O(1)
auto EdgeFlipping(HalfEdge *halfedge) {
    // ��¼��ľ�visitֵ
    auto visitvalue = halfedge->face->visit;
    // ����ת�����ڵ��ı��εĶ���
    auto v1 = halfedge->start;
    auto v2 = halfedge->twin->suc->end;
    auto v3 = halfedge->end;
    auto v4 = halfedge->suc->end;
    // ���������
    auto p1 = v1->point;
    auto p2 = v2->point;
    auto p3 = v3->point;
    auto p4 = v4->point;
    // ����ת�����ڵ��ı��εıߣ�ei��vi����
    auto e1 = halfedge->twin->suc;
    auto e2 = halfedge->twin->pre;
    auto e3 = halfedge->suc;
    auto e4 = halfedge->pre;
    // �ɵ���;ɵı�
    auto oldhalfedge1 = halfedge;
    auto oldhalfedge2 = halfedge->twin;
    auto oldface1 = oldhalfedge1->face;
    auto oldface2 = oldhalfedge2->face;
    // �޸Ķ��������ı�Ϊ�Ƿ�ת�ıߣ�����ת�����ڵ��ı��εıߣ�
    v1->halfedge = e1;
    v2->halfedge = e2;
    v3->halfedge = e3;
    v4->halfedge = e4;

    // ����ת�����ڵ��ı��ε�����Ͱ�еĵ�
    auto partps1 = halfedge->face->bucket->points;
    auto partps2 = halfedge->twin->face->bucket->points;
    // ���·�Ͱ
    vector<Point>newpoints1, newpoints2;
    for(auto each= partps1.begin();each!= partps1.end();++each){
        if (cross2(p2, p4, *each) > 0)
            newpoints1.push_back(*each);
        else
            newpoints2.push_back(*each);
    }
    for (auto each = partps2.begin();each != partps2.end();++each) {
        if (cross2(p2, p4, *each) > 0)
            newpoints1.push_back(*each);
        else
            newpoints2.push_back(*each);
    }

    // ���¹�����棬��ʱ��
    /*auto pnewface1 = Face(e1), pnewface2 = Face(e2);
    auto newface1 = &pnewface1, newface2 = &pnewface2;*/
    auto newface1 = new Face(e1), newface2 = new Face(e2);
    newface1->visit = visitvalue;
    newface2->visit = visitvalue;

    // ���췭ת��ı�
    /*auto pe5 = HalfEdge(v2, v4), pe6 = HalfEdge(v4, v2);
    auto e5 = &pe5, e6 = &pe6;*/
    auto e5 = new HalfEdge(v2, v4), e6 = new HalfEdge(v4, v2);
    e5->twin = e6;
    e6->twin = e5;
    e5->visit = visitvalue;
    e6->visit = visitvalue;

    // ����newface1�ı�
    e1->suc = e5;
    e5->suc = e4;
    e4->suc = e1;
    e1->pre = e4;
    e4->pre = e5;
    e5->pre = e1;
    // ����newface2�ı�
    e2->suc = e3;
    e3->suc = e6;
    e6->suc = e2;
    e2->pre = e6;
    e6->pre = e3;
    e3->pre = e2;

    // ��ָ��newface1
    e1->face = newface1;
    e4->face = newface1;
    e5->face = newface1;
    // ��ָ��newface2
    e2->face = newface2;
    e3->face = newface2;
    e6->face = newface2;

    // ����������Ͱ����ά��Ͱ�������ϵ
    /*auto pbucket1 = Bucket(newpoints1);
    auto pbucket2 = Bucket(newpoints2);
    
    auto bucket1 = &pbucket1;
    auto bucket2 = &pbucket2;*/

    auto bucket1 = new Bucket(newpoints1);
    auto bucket2 = new Bucket(newpoints2);

    bucket1->face = newface1;
    bucket2->face = newface2;
    newface1->bucket = bucket1;
    newface2->bucket = bucket2;
}

// ��vo˺����face��O(1)
auto ClipFace(Face* face, Vertice *vo, vector<Point> remainedpoints) {
    auto visitvalue = face->visit;
    auto hf1 = face->halfedge;
    auto hf2 = hf1->suc;
    auto hf3 = hf2->suc;

    // ������
    /*auto pclipface1 = Face(hf1);
    auto pclipface2 = Face(hf2);
    auto pclipface3 = Face(hf3);

    auto clipface1 = &pclipface1;
    auto clipface2 = &pclipface2;
    auto clipface3 = &pclipface3;*/

    auto clipface1 = new Face(hf1);
    auto clipface2 = new Face(hf2);
    auto clipface3 = new Face(hf3);

    clipface1->visit = visitvalue;
    clipface2->visit = visitvalue;
    clipface3->visit = visitvalue;

    // face1
    /*auto phf1_pre = HalfEdge(vo, hf1->start);
    auto phf1_suc = HalfEdge(hf1->end, vo);

    auto hf1_pre = &phf1_pre;
    auto hf1_suc = &phf1_suc;*/

    auto hf1_pre = new HalfEdge(vo, hf1->start);
    auto hf1_suc = new HalfEdge(hf1->end, vo);

    hf1_pre->visit = visitvalue;
    hf1_suc->visit = visitvalue;
    hf1->pre = hf1_pre;
    hf1->suc = hf1_suc;
    hf1_pre->pre = hf1_suc;
    hf1_pre->suc = hf1;
    hf1_suc->pre = hf1;
    hf1_suc->suc = hf1_pre;
    hf1->face = clipface1;
    hf1_pre->face = clipface1;
    hf1_suc->face = clipface1;

    // face2
    /*auto phf2_pre = HalfEdge(vo, hf2->start);
    auto phf2_suc = HalfEdge(hf2->end, vo);

    auto hf2_pre = &phf2_pre;
    auto hf2_suc = &phf2_suc;*/

    auto hf2_pre = new HalfEdge(vo, hf2->start);
    auto hf2_suc = new HalfEdge(hf2->end, vo);

    hf2_pre->visit = visitvalue;
    hf2_suc->visit = visitvalue;
    hf2->pre = hf2_pre;
    hf2->suc = hf2_suc;
    hf2_pre->pre = hf2_suc;
    hf2_pre->suc = hf2;
    hf2_suc->pre = hf2;
    hf2_suc->suc = hf2_pre;
    hf2->face = clipface2;
    hf2_pre->face = clipface2;
    hf2_suc->face = clipface2;

    // face3
    /*auto phf3_pre = HalfEdge(vo, hf3->start);
    auto phf3_suc = HalfEdge(hf3->end, vo);

    auto hf3_pre = &phf3_pre;
    auto hf3_suc = &phf3_suc;*/

    auto hf3_pre = new HalfEdge(vo, hf3->start);
    auto hf3_suc = new HalfEdge(hf3->end, vo);

    hf3_pre->visit = visitvalue;
    hf3_suc->visit = visitvalue;
    hf3->pre = hf3_pre;
    hf3->suc = hf3_suc;
    hf3_pre->pre = hf3_suc;
    hf3_pre->suc = hf3;
    hf3_suc->pre = hf3;
    hf3_suc->suc = hf3_pre;
    hf3->face = clipface3;
    hf3_pre->face = clipface3;
    hf3_suc->face = clipface3;

    // vo
    vo->halfedge = hf1_pre;

    // twin
    hf1_pre->twin = hf3_suc;
    hf3_suc->twin = hf1_pre;

    hf2_pre->twin = hf1_suc;
    hf1_suc->twin = hf2_pre;

    hf3_pre->twin = hf2_suc;
    hf2_suc->twin = hf3_pre;

    // �����Ͱ
    // Ͱ���������εĶ���
    Point point = vo->point;
    auto p1 = hf1->start->point;
    auto p2 = hf2->start->point;
    auto p3 = hf3->start->point;

    // ���Ͱ
    vector<Point> clipbucketps1, clipbucketps2, clipbucketps3;
    for (auto each = remainedpoints.begin();each != remainedpoints.end();++each) {
        if (InTriangle(p1, p2, point, *each))
            clipbucketps1.push_back(*each);
        else if (InTriangle(p2, p3, point, *each))
            clipbucketps2.push_back(*each);
        else
            clipbucketps3.push_back(*each);
    }
    
    // ˺�ѵ�ƽ�����Ͱ
    /*auto pclipbucket1 = Bucket(clipbucketps1);
    auto pclipbucket2 = Bucket(clipbucketps2);
    auto pclipbucket3 = Bucket(clipbucketps3);

    auto clipbucket1 = &pclipbucket1;
    auto clipbucket2 = &pclipbucket2;
    auto clipbucket3 = &pclipbucket3;*/

    auto clipbucket1 = new Bucket(clipbucketps1);
    auto clipbucket2 = new Bucket(clipbucketps2);
    auto clipbucket3 = new Bucket(clipbucketps3);

    clipface1->bucket = clipbucket1;
    clipface2->bucket = clipbucket2;
    clipface3->bucket = clipbucket3;
    clipbucket1->face = clipface1;
    clipbucket2->face = clipface2;
    clipbucket3->face = clipface3;

    return vector<Face*>{ clipface1, clipface2, clipface3 };
};

// ��������O(n)
auto VisitNet(Face* face) {
    auto visitvalue = face->visit;
    auto notvisitvalue = !visitvalue;
    vector<Face*>faces{ face };
    // ���ʹ�
    face->visit = notvisitvalue;

    vector<pair<Point, Point>>delaunaynet;

    while (!faces.empty()) {
        auto eachface = faces.back();
        faces.pop_back();
        // �����ڵ�������
        auto e1 = eachface->halfedge;
        auto e2 = e1->suc;
        auto e3 = e2->suc;
        // �����ڷ��ʵ�����������ڵ������faces
        vector<HalfEdge*> eis{ e1, e2, e3 };
        for (auto ei = eis.begin();ei != eis.end();++ei) {
            // ei�������ֵ�
            auto eiTwin = (*ei)->twin;
            // eiδ�����ʹ�
            if ((*ei)->visit == visitvalue) {
                auto ls = (*ei)->start->point, le = (*ei)->end->point;
                if (ls[2] != Infinity && le[2] != Infinity)
                    delaunaynet.push_back({ ls, le });
                (*ei)->visit = notvisitvalue;
                // if eiTwin: # ������Щԭ�ȶ��������if,�������ڳ�����Ķ������һ�������棨��ά̯������ά���Ǹ������棩
                faces.push_back(eiTwin->face);
                // ���ʹ�
                eiTwin->face->visit = notvisitvalue;
                eiTwin->visit = notvisitvalue;
            }
        }
    }
    return delaunaynet;
};

// ���������Σ�O(n)
auto VisitTriangles(Face* face) {
    // ������
    auto visitvalue = face->visit;
    auto notvisitvalue = !visitvalue;
    vector<Face*>faces{ face };
    // ���ʹ�
    face->visit = notvisitvalue;
    vector<vector<Point>>delaunaynet;

    while (!faces.empty()) {
        auto eachface = faces.back();
        faces.pop_back();
        // �����ڵ�������
        auto e1 = eachface->halfedge;
        auto e2 = e1->suc;
        auto e3 = e2->suc;
        // ��Ƿ��ʹ�
        e1->visit = notvisitvalue;
        e2->visit = notvisitvalue;
        e3->visit = notvisitvalue;
        // ���������
        auto p1 = e1->start->point;
        auto p2 = e2->start->point;
        auto p3 = e3->start->point;
        delaunaynet.push_back({ p1, p2, p3 });
        // �����ڷ��ʵ�����������ڵ������faces
        vector<HalfEdge*> eis{ e1, e2, e3 };
        for (auto ei = eis.begin();ei != eis.end();++ei) {
            auto et = (*ei)->twin;
            if (et != nullptr) {
                auto etf = et->face;
                // δ���ʹ�
                if(etf->visit == visitvalue){
                    // ���ʹ�
                    etf->visit = notvisitvalue;
                    faces.push_back(etf);
                }
            }
        }
    }
    return delaunaynet;
};
 
// ����άŵͼ��O(n)
auto VisitVoronoi(Face* face) {
    // ������
    auto visitvalue = face->visit;
    auto notvisitvalue = !visitvalue;
    vector<Face*>faces{ face };
    // ���ʹ�
    face->visit = notvisitvalue;

    vector<pair<Point, Point>>voronoi;

    while (!faces.empty()) {
        auto eachface = faces.back();
        faces.pop_back();
        // �����ڵ�������
        auto e1 = eachface->halfedge;
        auto e2 = e1->suc;
        auto e3 = e2->suc;
        // �����ڷ��ʵ�����������ڵ������faces
        vector<HalfEdge*> eis{ e1, e2, e3 };
        for (auto ei = eis.begin();ei != eis.end();++ei) {
            // ei�������ֵ�
            auto eiTwin = (*ei)->twin;
            //eiδ�����ʹ�
            if ((*ei)->visit == visitvalue) {
                (*ei)->visit = notvisitvalue;
                // if eiTwin: # ������Щԭ�ȶ��������if,�������ڳ�����Ķ������һ�������棨��ά̯������ά���Ǹ������棩
                auto ls = (*ei)->start->point, le = (*ei)->end->point;
                if (ls[2] != Infinity && le[2] != Infinity) {
                    auto efc = (*ei)->face->center, etfc = eiTwin->face->center;
                    auto ese = eiTwin->suc->end->point;
                    // �ߵĶԵ��������
                    if (ese[2] == Infinity) {
                        auto eis = np.array((*ei)->start->point), eie = np.array((*ei)->end->point);
                        auto vertical = np.cross(eie - eis, np.array({ 0, 0, 1 }));
                        vertical = np.normalize(vertical);
                        vertical = Infinity * vertical;
                        auto newle = efc + vertical;
                        voronoi.push_back({ efc, newle });
                    }
                    else
                        voronoi.push_back({ efc, etfc });
                }
                faces.push_back(eiTwin->face);
                // ���ʹ�
                eiTwin->face->visit = notvisitvalue;
                eiTwin->visit = notvisitvalue;
            }
        }
    }
    return voronoi;
};

// ������Բ�ģ�O(n)
auto InitNetCircumcircleCenter(Face* face) {
    // ������
    auto visitvalue = face->visit;
    auto notvisitvalue = !visitvalue;
    vector<Face*>faces{ face };
    // ���ʹ�
    face->visit = notvisitvalue;

    while (!faces.empty()) {
        auto eachface = faces.back();
        faces.pop_back();
        // �����ڵ�������
        auto e1 = eachface->halfedge;
        auto e2 = e1->suc;
        auto e3 = e2->suc;
        // ��Ƿ��ʹ�
        e1->visit = notvisitvalue;
        e2->visit = notvisitvalue;
        e3->visit = notvisitvalue;
        // ���������
        auto p1 = e1->start->point;
        auto p2 = e2->start->point;
        auto p3 = e3->start->point;
        // ��ֵԲ��
        if ((eachface->center)[0] == Infinity)
            eachface->center = CircumcircleCenter(p1, p2, p3);

        vector<HalfEdge*> eis{ e1, e2, e3 };
        for (auto ei = eis.begin();ei != eis.end();++ei) {
            auto eit = (*ei)->twin;
            if (eit != nullptr) {
                auto eitf = eit->face;
                // δ���ʹ�
                if (eitf->visit == visitvalue) {
                    // ���ʹ�
                    eitf->visit = notvisitvalue;
                    faces.push_back(eitf);
                }
            }
        }
    }
};

// ��������O(nlogn)
auto ConstructNet(vector<Point>points) {
    auto face1 = InitInfNet(points);
    auto infedge = face1->halfedge;
    vector<Bucket*>buckets{ face1->bucket };

    while (!buckets.empty()) {
        // ȡͰ
        auto bucket = buckets.back();
        buckets.pop_back();

        // ���Ϊ������
        if (bucket->visit)
            continue;
        bucket->visit = true;

        // ȡͰ�ĵ�
        auto point = bucket->points.back();
        bucket->points.pop_back();
        
        /*auto pvo = Vertice(point);
        auto vo = &pvo;*/

        auto vo = new Vertice(point);

        // Ͱ���������εı�
        auto crpface = bucket->face;
        auto hf1 = crpface->halfedge;
        auto hf2 = hf1->suc;
        auto hf3 = hf2->suc;

        // ˺����
        ClipFace(crpface, vo, bucket->points);
        // �����Ƿ�Ҫ�߷�ת
        vector<HalfEdge*>edges{ hf1, hf2, hf3 };
        while (!edges.empty()) {
            auto eachedge = edges.back();
            edges.pop_back();
            auto eachedgetwin = eachedge->twin;
            if (eachedgetwin != nullptr) {
                auto trip1 = vo->point;
                auto trip2 = eachedgetwin->start->point;
                auto trip3 = eachedgetwin->end->point;
                auto trip4 = eachedgetwin->suc->end->point;
                if (InCircle(trip1, trip2, trip3, trip4)) {
                    auto etfb = eachedgetwin->face->bucket;
                    if (etfb->points.size() > 0)
                        etfb->visit = true;
                    edges.push_back(eachedgetwin->pre);
                    edges.push_back(eachedgetwin->suc);
                    EdgeFlipping(eachedge);
                }
            }
        }

        // ��������Χ�����бߣ���Ͱ����
        auto ringvisit = vo->halfedge;
        auto currvisit = ringvisit->twin->suc;
        while (currvisit != ringvisit) {
            auto currbucket = currvisit->face->bucket;
            if (currbucket->points.size() > 0)
                buckets.push_back(currbucket);
            currvisit = currvisit->twin->suc;
        }
        auto currbucket = currvisit->face->bucket;
        if (currbucket->points.size() > 0)
            buckets.push_back(currbucket);
    }

    return infedge->face;
};

// �õ�ĳ�������е���
auto get_point_posface(Point point, Face* net) {
    // ������
    // ������
    auto visitvalue = net->visit;
    auto notvisitvalue = !visitvalue;
    vector<Face*>faces{ net };
    // ���ʹ�
    net->visit = notvisitvalue;

    // λ��
    auto posface = new Face(net->halfedge);
    auto mark = true;

    while (!faces.empty()) {
        auto eachface = faces.back();
        faces.pop_back();
        // �����ڵ�������
        auto e1 = eachface->halfedge;
        auto e2 = e1->suc;
        auto e3 = e2->suc;
        // ��Ƿ��ʹ�
        e1->visit = notvisitvalue;
        e2->visit = notvisitvalue;
        e3->visit = notvisitvalue;
        // ���������
        auto p1 = e1->start->point;
        auto p2 = e2->start->point;
        auto p3 = e3->start->point;
        // λ��δ�ҵ�
        if (mark)
            if (InTriangle(p1, p2, p3, point))
                posface = eachface;
        vector<HalfEdge*> eis{ e1, e2, e3 };
        for (auto ei = eis.begin();ei != eis.end();++ei) {
            auto eit = (*ei)->twin;
            if (eit != nullptr) {
                auto eitf = eit->face;
                // δ���ʹ�
                if (eitf->visit == visitvalue) {
                    // ���ʹ�
                    eitf->visit = notvisitvalue;
                    faces.push_back(eitf);
                }
            }
        }
    }
    return posface;
};

// �����в���㣬O(n)
auto net_insert_point(Point point, Face* net) {
    // �����ڵ���
    auto posface = get_point_posface(point, net);
    posface->bucket->points.push_back(point);
    auto infedge = posface->halfedge;
    vector<Bucket*>buckets{ posface->bucket };

    while (!buckets.empty()) {
        // ȡͰ
        auto bucket = buckets.back();
        buckets.pop_back();

        // ȡͰ�ĵ�
        auto point = bucket->points.back();
        bucket->points.pop_back();
        /*auto pvo = Vertice(point);
        auto vo = &pvo;*/
        auto vo = new Vertice(point);

        // Ͱ���������εı�
        auto crpface = bucket->face;
        auto hf1 = crpface->halfedge;
        auto hf2 = hf1->suc;
        auto hf3 = hf2->suc;

        // ˺����
        ClipFace(crpface, vo, bucket->points);
        // �����Ƿ�Ҫ�߷�ת
        vector<HalfEdge*>edges{ hf1, hf2, hf3 };
        while (!edges.empty()) {
            auto eachedge = edges.back();
            edges.pop_back();
            auto eachedgetwin = eachedge->twin;
            if (eachedgetwin != nullptr) {
                auto trip1 = vo->point;
                auto trip2 = eachedgetwin->start->point;
                auto trip3 = eachedgetwin->end->point;
                auto trip4 = eachedgetwin->suc->end->point;
                if (InCircle(trip1, trip2, trip3, trip4)) {
                    auto etfb = eachedgetwin->face->bucket;
                    if (etfb->points.size() > 0) {
                        for (auto itor = buckets.begin();itor != buckets.end();++itor) {
                            if (*itor == etfb)
                            {
                                buckets.erase(itor);
                                break;
                            }
                        }
                    }
                    edges.push_back(eachedgetwin->pre);
                    edges.push_back(eachedgetwin->suc);
                    EdgeFlipping(eachedge);
                }
            }
        }
        // ��������Χ�����бߣ���Ͱ����
        auto ringvisit = vo->halfedge;
        auto currvisit = ringvisit->twin->suc;
        while (currvisit != ringvisit) {
            auto currbucket = currvisit->face->bucket;
            if (currbucket->points.size() > 0)
                buckets.push_back(currbucket);
            currvisit = currvisit->twin->suc;
        }
        auto currbucket = currvisit->face->bucket;
        if (currbucket->points.size() > 0)
            buckets.push_back(currbucket);
    }
    return infedge->face;
};

// �����в���㣬���������ģ�O(n)
auto net_insert_point_and_set_circumcirclecenter(Point point, Face* net) {
    // �����ڵ��棬O(n)
    auto posface = get_point_posface(point, net);

    /*auto pvo = Vertice(point);
    auto vo = &pvo;*/
    auto vo = new Vertice(point);
    // Ͱ���������εı�
    auto crpface = posface;
    auto hf1 = crpface->halfedge;
    auto hf2 = hf1->suc;
    auto hf3 = hf2->suc;

    // ˺����
    ClipFace(crpface, vo, {});

    // ��������
    hf1->face->center = CircumcircleCenter(hf1->start->point, hf1->end->point, point);
    hf2->face->center = CircumcircleCenter(hf2->start->point, hf2->end->point, point);
    hf3->face->center = CircumcircleCenter(hf3->start->point, hf3->end->point, point);

    // �����Ƿ�Ҫ�߷�ת��O(6)
    vector<HalfEdge*>edges{ hf1, hf2, hf3 };
    while (!edges.empty()) {
        auto eachedge = edges.back();
        edges.pop_back();
        auto eachedgetwin = eachedge->twin;
        if (eachedgetwin != nullptr) {
            auto trip1 = vo->point;
            auto trip2 = eachedgetwin->start->point;
            auto trip3 = eachedgetwin->end->point;
            auto trip4 = eachedgetwin->suc->end->point;
            if (InCircle(trip1, trip2, trip3, trip4)) {
                edges.push_back(eachedgetwin->pre);
                edges.push_back(eachedgetwin->suc);
                auto efv1 = eachedge->suc;
                auto  efv2 = eachedgetwin->suc;
                EdgeFlipping(eachedge);
                efv1->face->center = CircumcircleCenter(trip1, trip2, trip4);
                efv2->face->center = CircumcircleCenter(trip1, trip3, trip4);
            }
        }
    }
    return vo->halfedge->face;
};

// ��������������O(nlogn)
class DelaunayTrianglation {
public:
    Face* net;
    vector<pair<Point, Point>>delaunaynet;
    // ��ȡ���Ķ���ԣ����������ʾ����
    auto VisitNet() {
        return ::VisitNet(this->net);
    };
    auto VisitTriangles() {
        return ::VisitTriangles(this->net);
    };
    // ��ȡ��
    auto GetNet() {
        return this->net;
    };
    // ��ȡ�����߹���
    auto GetDelaunaynet() {
        return this->delaunaynet;
    };
    // ����ڵ�
    auto InsertPoint(Point point) {
        ::net_insert_point(point, this->net);
        this->delaunaynet = this->VisitNet();
        return this->delaunaynet;
    };
    DelaunayTrianglation(vector<Point>points) {
        this->net = ::ConstructNet(points);
        this->delaunaynet = this->VisitNet();
    };
};

// άŵͼ��O(n) + O(nlogn) = O(nlogn)
class Voronoi {
public:
    Face* net;
    vector<pair<Point, Point>>voronoi;
    auto VisitVoronoi() {
        return ::VisitVoronoi(this->net);
    };
    // ��ȡ��
    auto GetNet() {
        return this->net;
    };
    // ��ȡ�����߹���
    auto GetVoronoi() {
        return this->voronoi;
    };
    // ����ڵ�
    auto InsertPoint(Point point) {
        net_insert_point_and_set_circumcirclecenter(point, this->net);
        this->voronoi = this->VisitVoronoi();
        return this->voronoi;
    };
    Voronoi(vector<Point>points) {
        this->net = DelaunayTrianglation(points).GetNet();
        InitNetCircumcircleCenter(this->net);
        this->voronoi = this->VisitVoronoi();
    };
};

// #pragma once
